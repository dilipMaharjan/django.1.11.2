from django.conf.urls import url
from .views import RestaurantListView,RestaurantDetailView,RestaurantLocationCreateView
    
urlpatterns = [
    url(r'^$', RestaurantListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    # url(r'^restaurants/(?P<pk>\d+)/$', RestaurantDetailView.as_view()),
    url(r'^create/$',RestaurantLocationCreateView.as_view())
    ]