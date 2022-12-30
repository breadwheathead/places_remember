from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from mainapp.views import MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('remembers/', include('remembersapp.urls', namespace='remembers')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

