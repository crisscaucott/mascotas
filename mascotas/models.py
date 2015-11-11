from django.db import models

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length = 30)

	class Meta:
		db_table = 'usuario'

	def __unicode__(self):
		return self.nombre

class Mascota(models.Model):
	nombre = models.CharField(max_length = 30)
	fecha_creacion = models.DateTimeField(auto_now_add = True)
	raza = models.CharField(max_length = 20)
	color = models.CharField(max_length = 20)
	sexo = models.CharField(max_length = 15)
	# Dueno
	usuario = models.ForeignKey(Usuario, blank = True, null = True)

	class Meta:
		db_table = 'mascota'

	def __unicode__(self):
		return self.nombre

class MascotasPerdidas(models.Model):
	mascota = models.ForeignKey(Mascota)
	fecha_perdido = models.DateTimeField(blank = False, null = False)
	fecha_encontrado = models.DateTimeField(blank = True, null = True)
	# Direccion donde se perdio la mascota
	dir_perdido = models.CharField(max_length = 60, blank = False, null = False)
	# Direccion donde se encontre la mascota
	dir_encontrado = models.CharField(max_length = 60, blank = True, null = True)
	recompensa = models.CharField(max_length = 20, blank=True, null = True)
	info_adicional = models.TextField()

	class Meta:
		db_table = 'mascotas_perdidas'

	def __unicode__(self):
		return self.mascota.nombre

class FotosMascota(models.Model):
	mascota = models.ForeignKey(Mascota)
	imagen = models.CharField(max_length = 200)

	class Meta:
		db_table = 'fotos_mascota'

	def __unicode__(self):
		return self.mascota

class MascotaCazaRecompensa(models.Model):
	usuario = models.ForeignKey(Usuario)
	mascota_perdida = models.ForeignKey(MascotasPerdidas, blank = True, null = True)

	class Meta:
		db_table = 'mascota_cazarecompensa'

	def __unicode__(self):
		return self.usuario

class FotosCazaRecompensas(models.Model):
	mascota_caza = models.ForeignKey(MascotaCazaRecompensa)
	imagen = models.CharField(max_length = 200)

	class Meta:
		db_table = 'fotos_cazarecompensa'

	def __unicode__(self):
		return self.mascota_caza
