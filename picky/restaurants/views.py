from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        return {"title": "Home"}


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        return {"title": "About"}


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, *args, **kwargs):
        return {"title": "Contact"}
