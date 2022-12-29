from django.views.generic import ListView

from remembersapp.models import Remember


class RemembersListView(ListView):
    model = Remember
    extra_context = {'title': 'Воспоминания'}
    paginate_by = 10
    template_name = 'remembersapp/remembers.html'

    def get_queryset(self):
        return Remember.objects.filter(user=self.request.user.id)
