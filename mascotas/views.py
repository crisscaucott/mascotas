from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Mascota

# Create your views here.
class MascotaListView(ListView):
	model = Mascota
	template_name = 'mascotas/mascota_home.html'

mascota_list = MascotaListView.as_view()

class MascotaCreateView(CreateView):
	model = Mascota
	template_name = 'mascotas/mascota_crear.html'
	fields = '__all__'
	success_url = reverse_lazy('mascota_list')

mascota_crear = MascotaCreateView.as_view()