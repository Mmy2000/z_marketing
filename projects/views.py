from django.shortcuts import render , get_object_or_404
from .models import Projects , ProductImages
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