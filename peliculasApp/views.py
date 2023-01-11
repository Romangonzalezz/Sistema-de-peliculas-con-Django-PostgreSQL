from django.views.generic import ListView, DetailView, View
from .models import Pelicula
from django.contrib.auth.decorators import login_required
from .forms import PeliculaForm, UserCreationForm
from django.shortcuts import render, redirect



    
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
            print(form)
            form.save()
            return redirect('pelicula_list')
        return render(request, self.template_name, {'form': form})

class PeliculaList(ListView):
    model = Pelicula
    paginate_by = 2
    #context_object_name = ''
    

class PeliculaDetail(DetailView):
    model = Pelicula


class PeliculaGenero(ListView):
    model = Pelicula

    def get_queryset(self):
        self.genero = self.kwargs['genero']
        return Pelicula.objects.filter(genero=self.genero)
    
    def get_context_data(self, **kwargs):
        context = super(PeliculaGenero, self).get_context_data(**kwargs)
        context['pelicula_genero'] = self.genero
        return context