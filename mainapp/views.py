from django.views.generic import TemplateView


class MainPageView(TemplateView):
    extra_context = {'title': 'Главная'}
    template_name = 'mainapp/main.html'
