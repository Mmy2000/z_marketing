from django.shortcuts import render
from .models import Projects , ProductImages
# Create your views here.
def projects(request):
    projects = Projects.objects.prefetch_related('project_image').all()
    context = {
        'projects':projects
    }
    return render(request , 'projects.html' , context)

def project_details(request , slug):
    project = Projects.objects.get(slug = slug)
    context = {
        'project':project
    }
    return render(request , 'project_details.html' , context)