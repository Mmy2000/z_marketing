from django.db import models

# Create your models here.

class About(models.Model):
    what_we_do = models.TextField( max_length=5000)
    our_mission = models.TextField(max_length=5000)
    image = models.ImageField( upload_to='about/')

    def __str__(self):
        return str(self.id)
    
