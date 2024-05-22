from django.shortcuts import render
from service.models import Services
from about.models import About
from .models import NewsLitter
from django.http import JsonResponse

# Create your views here.

def home(request):
    services = Services.objects.all()[:4]
    about = About.objects.last()
    context = {
        'services':services,
        'about' : about
    }

    return render(request , 'home.html' , context)

def news_letters_subscribe(request):
    email = request.POST.get('emailinput')
    NewsLitter.objects.create(email=email)
    return JsonResponse({'done':'done'})