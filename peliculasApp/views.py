from django.views.generic import ListView, DetailView, View
from .models import Pelicula
from .forms import PeliculaForm,RegistrarUsuarioForm
from django.shortcuts import render, redirect
from django.contrib import messages

#Crear pelicula 
class PeliculaView(View):
    form_class = PeliculaForm
    template_name = 'peliculasApp/nueva_pelicula.html'


    #Obtener el template
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    #Crear pelicula
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('peliculasApp:pelicula_list')
        print(form)
        return render(request, self.template_name, {'form': form})

class PeliculaList(ListView):
    model = Pelicula
    paginate_by = 4
    #context_object_name = ''
    

class PeliculaDetail(DetailView):
    model = Pelicula


class PeliculaGenero(ListView):
    model = Pelicula
    paginate_by = 2

    def get_queryset(self):
        self.genero = self.kwargs['genero']
        return Pelicula.objects.filter(genero=self.genero)
    
    def get_context_data(self, **kwargs):
        context = super(PeliculaGenero, self).get_context_data(**kwargs)
        context['pelicula_genero'] = self.genero
        return context
    

class PeliculaBuscador(ListView):
    model = Pelicula
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(titulo__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list
        

def registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'peliculasApp/registrarse.html', {'form': form, 'title': 'registrese aquí'})

