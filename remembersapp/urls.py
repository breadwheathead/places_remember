from django.contrib.auth.decorators import login_required
from django.urls import path

from remembersapp.views import RemembersListView

app_name = 'remembersapp'

urlpatterns = [
    path('', login_required(RemembersListView.as_view()), name='remembers'),
]
