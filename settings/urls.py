from django.urls import path
from . import views

urlpatterns = [
    path( '',views.home , name='home' ),    
    path('newsletter/' ,views.news_letters_subscribe , name = 'newsletter'), 
]