from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """ View Main Page """
    extra_context = {'title': 'Главная'}
    template_name = 'mainapp/main.html'
