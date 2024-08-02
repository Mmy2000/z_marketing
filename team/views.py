from django.shortcuts import render
from .models import Team

# Create your views here.
def team(request):
    teams = Team.objects.all()
    return render(request , 'team.html' , {'teams':teams})