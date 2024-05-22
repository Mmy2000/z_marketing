from django.db import models

# Create your models here.
class Settings(models.Model):
    site_name = models.CharField( max_length=50)
    logo = models.ImageField( upload_to='setting/')
    phone = models.CharField( max_length=30)
    email = models.EmailField( max_length=254)
    description = models.TextField(max_length=1000)
    fb_link = models.URLField( max_length=200)
    linkedin_link = models.URLField( max_length=200)
    instagram_link = models.URLField( max_length=200)
    tiktok_link = models.URLField( max_length=200)
    address = models.CharField( max_length=50)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Info")

    def __str__(self):
        return self.site_name