from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pelicula



class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class PeliculaForm(forms.ModelForm):        
    #Form de pelicula
    class Meta:
        model = Pelicula
        fields= ['titulo', 'sinopsis',
                  'anio', 'genero', 'imagen']
    