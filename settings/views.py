from django.shortcuts import render
from service.models import Services
from about.models import About , Support
from .models import NewsLitter , Clients
from django.http import JsonResponse
from team.models import Team
from projects.models import Projects

# Create your views here.

def home(request):
    services = Services.objects.all()[:4]
    about = About.objects.last()
    teams = Team.objects.all()
    projects = Projects.objects.prefetch_related('project_image').all()
    supports = Support.objects.all()
    context = {
        'services':services,
        'about' : about,
        'teams' : teams,
        'projects' : projects,
        'supports' : supports,
    }

    return render(request , 'home.html' , context)

def news_letters_subscribe(request):
    email = request.POST.get('emailinput')
    NewsLitter.objects.create(email=email)
    return JsonResponse({'done':'done'})


