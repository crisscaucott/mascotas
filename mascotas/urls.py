from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.mascota_list, name = 'mascota_list'),
	url(r'^crear/$', views.mascota_crear, name = 'mascota_crear'),
	url(r'^caza-recompensas/$', views.caza_recompensas, name = 'caza_recompensas'),
	url(r'^caza-recompensas/borrar/(?P<pk>\d+)$', views.caza_recompensas_borrar, name = 'caza_recompensas_borrar'),
	url(r'^perdida/editar/(?P<pk>\d+)/$', views.p_mascota_editar, name = 'p_mascota_editar'),
]