from .models import Settings , Images

def myfooter(request):
    myfooter = Settings.objects.last()
    slider_images = Images.objects.all()
    return{'myfooter':myfooter,'slider_images':slider_images}