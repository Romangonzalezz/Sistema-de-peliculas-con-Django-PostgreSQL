from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', RedirectView.as_view(url='pelicula_list', permanent=False), name='index'),
    path('peliculas/', include('peliculasApp.urls', namespace = 'peliculas')),
    path('accounts/logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


