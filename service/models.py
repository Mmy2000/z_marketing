from django.db import models
from django.utils import timezone
from django.utils.text import slugify 

# Create your models here.
class Services(models.Model):
    name = models.CharField( max_length=50)
    icon = models.CharField(max_length=30)
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    description = models.TextField(("description"),max_length=100000,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Services,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
    