from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import RestaurantLocation
from django.views.generic import ListView, DetailView, CreateView
from .form import RestaurantLocationForm


def restaurant_list(request):
    template_name = 'restaurants/restaurantlocation_list.html'
    restaurants = RestaurantLocation.objects.all()
    return render(request, template_name, {"restaurants": restaurants})


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     return super(RestaurantDetailView, self).get_context_data(*args, **kwargs)

    # def get_object(self, *args, **kwargs):
    #     slug = self.kwargs.get('slug')
    #     return get_object_or_404(RestaurantLocation, slug=slug)


class RestaurantLocationCreateView(CreateView):
    form_class = RestaurantLocationForm
    template_name = "form.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantLocationCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantLocationCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context
