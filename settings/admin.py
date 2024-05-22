from django.contrib import admin
from .models import Settings , NewsLitter , Clients
# Register your models here.

admin.site.register(Settings)
admin.site.register(NewsLitter)
admin.site.register(Clients)