from django.urls import path, include
from .views import PeliculaList, PeliculaDetail, PeliculaView, PeliculaGenero, PeliculaBuscador
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'peliculasApp'

urlpatterns = [
    path('', PeliculaList.as_view(), name = 'pelicula_list'),
    path('nueva_pelicula', PeliculaView.as_view(), name='nueva_pelicula'),
    path('genero/<str:genero>', PeliculaGenero.as_view(), name='pelicula_genero'),
    path('<int:pk>', PeliculaDetail.as_view(), name = 'pelicula_detail'),
    path('buscar/', PeliculaBuscador.as_view(), name = 'buscar_pelicula'),
    path('registrarse/', views.registrarse, name='registrarse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)