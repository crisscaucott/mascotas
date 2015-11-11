from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.mascota_list, name = 'mascota_list'),
	url(r'^crear/$', views.mascota_crear, name = 'mascota_crear'),
]