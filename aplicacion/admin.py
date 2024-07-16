from django.contrib import admin
from .models import Hotel, TipoServicio, Evento, Servicio, TipoHabitacion, Habitacion, Pasajero, HabitacionReserva, Reserva, HistorialPrecios, Administrador, Oferta, OfertaReserva, OfertaServicio


class AdmTipoServicio(admin.ModelAdmin):
    list_display = ['nombre']


class AdmHotel(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion']


class AdmEvento(admin.ModelAdmin):
    list_display = ['nombre', 'capacidad', 'ingresos', 'hotel']


class AdmHabitacion(admin.ModelAdmin):
    list_display = ['numero', 'hotel', 'valor',
                    'cantidad_personas', 'cantidad_banos']


admin.site.register(TipoServicio, AdmTipoServicio)
admin.site.register(Hotel, AdmHotel)
admin.site.register(Evento, AdmEvento)
admin.site.register(Habitacion, AdmHabitacion)
