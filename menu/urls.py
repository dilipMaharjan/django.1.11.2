from django.conf.urls import url

from .views import ItemCreateView,ItemDetailView,ItemListView,ItemUpdateView
urlpatterns = [
    url(r'^$', ItemListView.as_view()),
    url(r'^create/$',ItemCreateView.as_view()),
    url(r'^(?P<id>\d+)/$', ItemDetailView.as_view()),
    url(r'^(?P<id>[d]+)/edit/$',ItemUpdateView.as_view())
]