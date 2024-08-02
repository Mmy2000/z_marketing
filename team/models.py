from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField( max_length=50)
    headline = models.CharField( max_length=100)
    fb_link = models.URLField( max_length=200)
    linkedin_link = models.URLField( max_length=200)
    instagram_link = models.URLField( max_length=200)
    twitter_link = models.URLField( max_length=200 , null=True , blank=True)
    image = models.ImageField( upload_to='team/')

    def __str__(self):
        return self.name
    