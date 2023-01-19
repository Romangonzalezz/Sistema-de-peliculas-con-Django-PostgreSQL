from .models import Pelicula 

def slider_peliculas(request):
    peliculas = Pelicula.objects.all().order_by('-creada')[0:3]
    return {'slider_peliculas' : peliculas}