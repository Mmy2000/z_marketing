from django.shortcuts import render
from .models import About , Support
# Create your views here.
def about(request):
    about = About.objects.last()
    supports = Support.objects.all()
    context = {
        'about':about,
        'supports':supports
    }
    return render(request , 'about.html' , context)