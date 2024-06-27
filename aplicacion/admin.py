from django.contrib import admin
from .models import *
# Register your models here.

from django.contrib import admin
from .models import Hotel, TipoServicio, Servicio, TipoHabitacion, Habitacion, Pasajero, HabitacionReserva, Reserva, HistorialPrecios, Administrador, Oferta, OfertaReserva, OfertaServicio

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'cantidad_habitaciones', 'capacidad_total')

@admin.register(TipoServicio)
class TipoServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('valor', 'descripcion', 'hotel', 'tipo_servicio')

@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'valor', 'hotel', 'cantidad_personas', 'cantidad_banos')

@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'numero')

@admin.register(HabitacionReserva)
class HabitacionReservaAdmin(admin.ModelAdmin):
    list_display = ('cantidad_servicios', 'servicio')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicio', 'fecha_final', 'habitacion', 'pasajero')

@admin.register(HistorialPrecios)
class HistorialPreciosAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicio', 'fecha_final', 'valor')

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')

@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicio', 'fecha_final', 'porcentaje_dcto')

@admin.register(OfertaReserva)
class OfertaReservaAdmin(admin.ModelAdmin):
    list_display = ('oferta', 'reserva')

@admin.register(OfertaServicio)
class OfertaServicioAdmin(admin.ModelAdmin):
    list_display = ('oferta', 'servicio')
