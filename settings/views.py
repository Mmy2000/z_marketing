from django.shortcuts import render
from service.models import Services
from about.models import About
# Create your views here.

def home(request):
    services = Services.objects.all()[:4]
    about = About.objects.last()
    context = {
        'services':services,
        'about' : about
    }

    return render(request , 'home.html' , context)