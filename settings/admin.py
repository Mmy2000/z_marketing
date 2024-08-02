from django.contrib import admin
from .models import Settings , NewsLitter , Images
# Register your models here.

admin.site.register(Settings)
admin.site.register(NewsLitter)
admin.site.register(Images)