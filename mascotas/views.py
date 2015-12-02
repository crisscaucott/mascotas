from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models.aggregates import Count
from .models import Mascota, MascotasPerdidas

# Create your views here.
class MascotaListView(ListView):
	model = Mascota
	template_name = 'mascotas/mascota_home.html'

	# Devuelve los datos de la tabla MascotasPerdidas
	def get_context_data(self, **kwargs):
	    context = super(MascotaListView, self).get_context_data(**kwargs)
	    context['m_perdidas'] = MascotasPerdidas.objects.filter(fecha_encontrado = None).select_related().all()

	    # Item 2, mascotas encontradas que ya hayan sido perdidas
	    # item2_ids = MascotasPerdidas.objects.values_list('mascota_id', flat = True).annotate(ids_mascotas=Count('mascota_id')).filter(ids_mascotas__gt = 1)
	    # print item2_ids
	    context['item2'] = MascotasPerdidas.objects.raw("""select *
				from mascotas_perdidas as mp, mascota as m
				where mp.mascota_id in (select mascota_id
				from mascotas_perdidas
				group by mascota_id
				having count(mascota_id) > 1)
				and (mp.fecha_perdido is not null and mp.fecha_encontrado is null)
				and m.id = mp.mascota_id
				""")
	    
	    return context;


mascota_list = MascotaListView.as_view()

class MascotaCreateView(CreateView):
	model = Mascota
	template_name = 'mascotas/mascota_crear.html'
	fields = '__all__'
	success_url = reverse_lazy('mascota_list')

mascota_crear = MascotaCreateView.as_view()