from django.contrib import admin
from .models import Projects , ProductImages , Booking
import admin_thumbnails
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProjectGallaryInline(admin.TabularInline):
    model = ProductImages
    extra = 1

class ModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines = [ProjectGallaryInline]

admin.site.register(Projects,ModelAdmin)
admin.site.register(ProductImages)
admin.site.register(Booking)

