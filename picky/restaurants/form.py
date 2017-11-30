from django import forms
from .models import RestaurantLocation

class RestaurantLocationForm(forms.ModelForm):
    """Form definition for RestaurantLocation."""
    
    class Meta:
        """Meta definition for RestaurantLocationform."""
    
        model = RestaurantLocation
        fields = ('name','location','category',)
    
