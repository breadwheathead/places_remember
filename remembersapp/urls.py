from django.contrib.auth.decorators import login_required
from django.urls import path

from remembersapp.views import RemembersListView, RememberAddView, RememberView, RememberDelView

app_name = 'remembersapp'

urlpatterns = [
    path('', login_required(RemembersListView.as_view()), name='remembers'),
    path('add/', login_required(RememberAddView.as_view()), name='add'),
    path('remember/<int:pk>/', login_required(RememberView.as_view()), name='remember'),
    path('delete/<int:pk>/', login_required(RememberDelView.as_view()), name='delete'),
]
