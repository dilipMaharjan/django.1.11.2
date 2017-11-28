from django.shortcuts import render
from .models import RestaurantLocation

def restaurant_list(request):
    template='restaurants/restaurant_list.html'
    restaurants=RestaurantLocation.objects.all()
    return render(request,template,{"restaurants":restaurants})