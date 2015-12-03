from django.contrib import admin
from .models import Mascota,MascotasPerdidas,FotosMascota,Usuario,MascotaCazaRecompensa,FotosCazaRecompensas

# Register your models here.
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'fecha_creacion', 'raza', 'color', 'sexo', 'usuario', 'animal']

@admin.register(MascotasPerdidas)
class MascotaPerdidasAdmin(admin.ModelAdmin):
	list_display = ['mascota', 'fecha_perdido', 'fecha_encontrado', 'dir_perdido', 'dir_encontrado', 'recompensa', 'info_adicional']

@admin.register(FotosMascota)
class FotosMascotaAdmin(admin.ModelAdmin):
	list_display = ['mascota', 'imagen']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['nombre']

@admin.register(MascotaCazaRecompensa)
class MascotaCazaRecompensaAdmin(admin.ModelAdmin):
	list_display = ['usuario']

@admin.register(FotosCazaRecompensas)
class FotosCazaRecompensasAdmin(admin.ModelAdmin):
	list_display = ['mascota_caza', 'imagen']