from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
from django.urls import reverse


# Create your models here.
class Projects(models.Model):
    name = models.CharField( max_length=50)
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    description = models.TextField(("description"),max_length=100000,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Projects,self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("project_details", args=[self.slug])

    class Meta:
        verbose_name = ("Projects")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return self.name
    
class ProductImages(models.Model):
    project = models.ForeignKey(Projects,related_name='project_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projectimages/')

    class Meta:
        verbose_name = ("Project Images")
        verbose_name_plural = ("Project Images")

    def __str__(self):
        return str(self.project)
    


class Booking(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=1)  # Add this line
    booking_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"Booking by {self.name} for {self.project.name} - Quantity: {self.quantity}"
