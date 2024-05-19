from django.db import models

# Create your models here.

CHOICES = (
    ("Beach", "Beach"),
    ("Mountain", "Mountain"),
    ("City", "City"),
    ("Historical", "Historical"),
)

class Destination(models.Model):
    name = models.CharField(max_length=200, default=1)
    country = models.CharField(max_length=200, default=1)
    description = models.TextField(default='')
    best_time_to_visit = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CHOICES, default="Beach")
    image_url = models.ImageField(upload_to='images', default='default_image.jpg')  
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
       

    def __str__(self):
        return self.name