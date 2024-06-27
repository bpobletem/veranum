from django.contrib import admin
from .models import Hotel, TipoServicio, Servicio, TipoHabitacion, Habitacion, Pasajero, HabitacionReserva, Reserva, HistorialPrecios, Administrador, Oferta, OfertaReserva, OfertaServicio

class AdmTipoServicio(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(TipoServicio, AdmTipoServicio)