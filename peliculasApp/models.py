from django.db import models

GENEROS_CHOICES = [ 
    ('accion', 'Accion'),
    ('aventura', 'Aventura'),
    ('animacion', 'Animacion'),
    ('drama', 'Drama'),
    ('ciencia ficcion', 'Ciencia Ficcion'),
    ('terror', 'Terror'),
    ('misterio', 'Misterio'),
]

STATUS_CHOICES = [ 
    ('recientemente anidada', 'Recientemente anidada'),
    ('mas vista', 'Mas vista'),
    ('mas valorada', 'Mas valorada'),
]

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    sinopsis = models.TextField(max_length=1000)
    anio = models.DateField()
    imagen = models.ImageField(upload_to='peliculas')
    genero = models.CharField(choices=GENEROS_CHOICES, max_length=15)
    status = models.CharField(choices=STATUS_CHOICES, max_length=22)

    def __str__(self):
        return self.titulo
