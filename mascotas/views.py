from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models.aggregates import Count
import pprint
from .models import Mascota, MascotasPerdidas, MascotaCazaRecompensa, FotosCazaRecompensas

# Create your views here.
class MascotaListView(ListView):
	model = Mascota
	template_name = 'mascotas/mascota_home.html'

	# Devuelve los datos de la tabla MascotasPerdidas
	def get_context_data(self, **kwargs):
	    context = super(MascotaListView, self).get_context_data(**kwargs)
	    context['m_perdidas'] = MascotasPerdidas.objects.filter(fecha_encontrado = None).select_related().all()
	    context['m_perdidas_todas'] = MascotasPerdidas.objects.filter().select_related().all()

	    # Item 2, mascotas encontradas que ya hayan sido perdidas
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

# ITEM 3
class MascotasPerdidasUpdateView(UpdateView):
	model = MascotasPerdidas
	template_name = 'mascotas/mascotas_perdidas_update.html'
	# SOLO SE PODRAN MODIFICAR ESTOS CAMPOS
	fields = ['fecha_encontrado', 'dir_encontrado', 'recompensa', 'info_adicional']
	success_url = reverse_lazy('mascota_list')

p_mascota_editar = MascotasPerdidasUpdateView.as_view()


class MascotaCazaRecompensaListView(CreateView):
	model = MascotaCazaRecompensa
	template_name = 'mascotas/caza_recompensas.html'
	fields = '__all__'

	def get_context_data(self, **kwargs):
	    context = super(MascotaCazaRecompensaListView, self).get_context_data(**kwargs)
	    context['mascota_caza'] = FotosCazaRecompensas.objects.select_related().filter(deleted_at = False).all()

	    return context

caza_recompensas = MascotaCazaRecompensaListView.as_view()

def caza_recompensas_borrar(request, pk, template_name = 'mascotas/caza_recompensas_borrar.html'):
	fotosCazaRecompensas = get_object_or_404(FotosCazaRecompensas, pk=pk)
	if request.method == 'POST':
		# HARD DELETE (borra el registro por completo)
		# fotosCazaRecompensas.delete()
		# SOFT DELETE (borrado logido del registro)
		fotosCazaRecompensas.deleted_at = True
		fotosCazaRecompensas.save()
		return redirect('caza_recompensas')
	return render(request, template_name, {'object' : fotosCazaRecompensas})


