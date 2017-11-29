from django.shortcuts import render

from .models import RestaurantLocation


def restaurant_list(request):
    template_name = 'restaurants/restaurantlocation_list.html'
    restaurants = RestaurantLocation.objects.all()
    return render(request, template_name, {"restaurants": restaurants})
