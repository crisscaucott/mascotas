from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Mascota, MascotasPerdidas

# Create your views here.
class MascotaListView(ListView):
	model = Mascota
	template_name = 'mascotas/mascota_home.html'

	# Devuelve los datos de la tabla MascotasPerdidas
	def get_context_data(self, **kwargs):
	    context = super(MascotaListView, self).get_context_data(**kwargs)
	    context['m_perdidas'] = MascotasPerdidas.objects.select_related().all()
	    return context;


mascota_list = MascotaListView.as_view()

class MascotaCreateView(CreateView):
	model = Mascota
	template_name = 'mascotas/mascota_crear.html'
	fields = '__all__'
	success_url = reverse_lazy('mascota_list')

mascota_crear = MascotaCreateView.as_view()