from django.shortcuts import render
from .models import About
# Create your views here.
def about(request):
    about = About.objects.last()
    context = {
        'about':about
    }
    return render(request , 'about.html' , context)