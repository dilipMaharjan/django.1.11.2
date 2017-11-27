from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home.html', {"title": "Home"})


def about(request):
    return render(request, 'about.html', {"title": "About"})


def contact(request):
    return render(request, 'contact.html', {"title": "Contact"})


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html', {"title": "Contact"})


class ContactTemplateView(TemplateView):
        template_name = 'contact.html'
