from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class MainPageView(TemplateView):
    extra_context = {'title': 'Главная'}
    template_name = 'mainapp/main.html'
