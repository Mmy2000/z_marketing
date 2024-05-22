from django.db import models

# Create your models here.

class About(models.Model):
    what_we_do = models.TextField( max_length=5000)
    our_mission = models.TextField(max_length=5000)
    image = models.ImageField( upload_to='about/')

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("About")

    def __str__(self):
        return str(self.id)
    
