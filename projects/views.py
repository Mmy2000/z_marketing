from django.shortcuts import render , get_object_or_404 , redirect
from .models import Projects , ProductImages
from .forms import BookingForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def projects(request):
    projects = Projects.objects.prefetch_related('project_image').all()
    context = {
        'projects':projects
    }
    return render(request , 'projects.html' , context)

def project_details(request , slug):
    project = get_object_or_404(Projects, slug=slug)
    context = {
        'project':project
    }
    return render(request , 'project_details.html' , context)

def project_details(request, slug):
    project = get_object_or_404(Projects, slug=slug)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.project = project
            booking.save()
            name = form.cleaned_data['name']
            subject = f"Hi {name} Welcome to AI Control site"
            message = "Our team will contact you within 24hrs for Booking confirmation."
            email_from = settings.EMAIL_HOST_USER
            email = form.cleaned_data['email']
            
            recipient_list =email
            send_mail(subject, message, email_from, [recipient_list])
            # You can add a success message here
            messages.success(request, 'Your Product Booked successfully.')
            return redirect('project_details', slug=project.slug)
    else:
        form = BookingForm()

    return render(request, 'project_details.html', {'project': project, 'form': form})