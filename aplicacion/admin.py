from django.contrib import admin
from .models import Hotel, TipoServicio, Servicio, Evento, TipoHabitacion, Habitacion, Pasajero, HabitacionReserva, Reserva, HistorialPrecios, Administrador, Oferta, OfertaReserva, OfertaServicio


class AdmTipoServicio(admin.ModelAdmin):
    list_display = ['nombre']

class AdmHotel(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion']

class AdmEvento(admin.ModelAdmin):
    list_display = ['nombre', 'capacidad', 'ingresos', 'hotel']


admin.site.register(Hotel, AdmHotel)
admin.site.register(TipoServicio, AdmTipoServicio)
admin.site.register(Servicio)
admin.site.register(TipoHabitacion)
admin.site.register(Habitacion)
admin.site.register(Pasajero)
admin.site.register(HabitacionReserva)
admin.site.register(Reserva)
admin.site.register(HistorialPrecios)
admin.site.register(Administrador)
admin.site.register(Oferta)
admin.site.register(OfertaReserva)
admin.site.register(OfertaServicio)
admin.site.register(Evento, AdmEvento)
