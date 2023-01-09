from django.urls import path

from remembersapp.views import RemembersListView, RememberAddView, RememberView, RememberDelView

app_name = 'remembersapp'

urlpatterns = [
    path('', RemembersListView.as_view(), name='remembers'),
    path('add/', RememberAddView.as_view(), name='add'),
    path('remember/<int:pk>/', RememberView.as_view(), name='remember'),
    path('delete/<int:pk>/', RememberDelView.as_view(), name='delete'),
]
