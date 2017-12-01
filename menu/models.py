from django.db import models
from django.conf import settings
from restaurants.models import RestaurantLocation

class Item(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant=models.ForeignKey(RestaurantLocation)
    name = models.CharField(max_length=50)
    contents = models.TextField(help_text='Separate with comma')
    excludes = models.TextField(blank=True,null=True,help_text='Separate with comma')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-timestamp','-updated']
  
