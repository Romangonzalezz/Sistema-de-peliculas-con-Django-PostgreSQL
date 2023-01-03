from django.db import models

GENEROS_CHOICES = [ 
    ('AC', 'Accion'),
    ('AV', 'Aventura'),
    ('AN', 'Animacion'),
    ('DR', 'Drama'),
    ('CF', 'Ciencia Ficcion'),
    ('TE', 'Terror'),
    ('MI', 'Misterio'),
]

STATUS_CHOICES = [ 
    ('RA', 'Recientemente anidada'),
    ('MV', 'Mas vista'),
    ('TV', 'Mas valorada'),
]

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    sinopsis = models.TextField(max_length=1000)
    anio = models.DateField()
    imagen = models.ImageField(upload_to='peliculas')
    genero = models.CharField(choices=GENEROS_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)

    def __str__(self):
        return self.titulo
