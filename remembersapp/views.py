from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from django.conf import settings
from remembersapp.forms import RememberAddForm
from remembersapp.models import Remember


class RemembersListView(ListView):
    model = Remember
    extra_context = {'title': 'Воспоминания'}
    paginate_by = 10
    template_name = 'remembersapp/remembers.html'

    def get_queryset(self):
        return Remember.objects.filter(user=self.request.user.id)


class RememberAddView(CreateView):
    model = Remember
    extra_context = {'title': 'Добавить Воспоминание'}
    form_class = RememberAddForm
    success_url = reverse_lazy('remembers:remembers')
    template_name = 'remembersapp/remember_add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apikey'] = settings.YA_MAP_API_KEY
        return context


class RememberView(DetailView):
    model = Remember
    extra_context = {'title': 'Воспоминание'}
    template_name = 'remembersapp/remember.html'


class RememberDelView(DeleteView):
    model = Remember
    template_name = 'remembersapp/remember.html'
    success_url = reverse_lazy('remembers:remembers')
