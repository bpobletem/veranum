from django.contrib import admin
from .models import Hotel, TipoServicio, Servicio, Evento, TipoHabitacion, Habitacion, Pasajero, HabitacionReserva, Reserva, HistorialPrecios, Administrador, Oferta, OfertaReserva, OfertaServicio


class AdmTipoServicio(admin.ModelAdmin):
    list_display = ['nombre']


class AdmHotel(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion']


class AdmEvento(admin.ModelAdmin):
    list_display = ['nombre', 'capacidad', 'ingresos', 'hotel']


class AdmHabitacion(admin.ModelAdmin):
    list_display = ['numero', 'hotel', 'valor', 'cantidad_personas', 'cantidad_banos']


class AdmTipoHabitacion(admin.ModelAdmin):
    list_display = ['nombre']

class AdmPasajero(admin.ModelAdmin):
    list_display = ['nombre']

class AdmReserva(admin.ModelAdmin):
    list_display = ['fecha_inicio', 'fecha_final']


admin.site.register(Hotel, AdmHotel)
admin.site.register(TipoServicio, AdmTipoServicio)
admin.site.register(Evento, AdmEvento)
admin.site.register(Habitacion, AdmHabitacion)
admin.site.register(TipoHabitacion, AdmTipoHabitacion)
admin.site.register(Pasajero, AdmPasajero)
admin.site.register(Reserva, AdmReserva)