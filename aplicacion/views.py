from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import TipoServicio, Servicio, Hotel, Habitacion, Servicio, Reserva, Evento
from .forms import TipoServicioForm, ServicioForm
from datetime import datetime


def reportes(request):
    return render(request, 'aplicacion/reportes.html')


def reporte_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'aplicacion/reporte_habitaciones.html', {'habitaciones': habitaciones})


def reporte_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'aplicacion/reporte_servicios.html', {'servicios': servicios})


def reporte_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'aplicacion/reporte_reservas.html', {'reservas': reservas})


def tipo_servicio_list(request):
    servicios = TipoServicio.objects.all()
    return render(request, 'aplicacion/tipo_servicio_list.html', {'servicios': servicios})


def tipo_servicio_create(request):
    if request.method == 'POST':
        form = TipoServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de servicio creado con éxito')
            return redirect('tipo_servicio_list')
    else:
        form = TipoServicioForm()
    return render(request, 'aplicacion/tipo_servicio_form.html', {'form': form})


def tipo_servicio_update(request, id):
    servicio = get_object_or_404(TipoServicio, id=id)
    if request.method == 'POST':
        form = TipoServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de servicio modificado con éxito')
            return redirect('tipo_servicio_list')
    else:
        form = TipoServicioForm(instance=servicio)
    return render(request, 'aplicacion/tipo_servicio_form.html', {'form': form})


def tipo_servicio_delete(request, id):
    servicio = get_object_or_404(TipoServicio, id=id)
    if request.method == 'POST':
        servicio.delete()
        messages.success(request, 'Tipo de servicio eliminado con éxito')
        return redirect('tipo_servicio_list')
    return render(request, 'aplicacion/tipo_servicio_confirm_delete.html', {'servicio': servicio})


def crear_servicio(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio creado con éxito')
            return redirect('lista_servicios')
    else:
        form = ServicioForm()
    return render(request, 'aplicacion/crear_servicio.html', {'form': form})


def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'aplicacion/lista_servicios.html', {'servicios': servicios})


def editar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio modificado con éxito')
            return redirect('lista_servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'aplicacion/editar_servicio.html', {'form': form, 'servicio': servicio})


def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if request.method == "POST":
        servicio.delete()
        messages.success(request, 'Servicio eliminado con éxito')
        return redirect('lista_servicios')
    return render(request, 'aplicacion/eliminar_servicio.html', {'servicio': servicio})

def informe_eventos(request):
    hoteles = Hotel.objects.all()
    eventos = Evento.objects.select_related('hotel').all()

    # Obtener parámetros de filtrado
    hotel_id = request.GET.get('hotel')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_final = request.GET.get('fecha_final')

    # Aplicar filtros
    if hotel_id:
        eventos = eventos.filter(hotel_id=hotel_id)
    if fecha_inicio:
        fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_inicio = fecha_inicio_dt.strftime('%d/%m/%Y')
        eventos = eventos.filter(fecha_inicio__gte=fecha_inicio_dt)
    if fecha_final:
        fecha_final_dt = datetime.strptime(fecha_final, '%Y-%m-%d')
        fecha_final = fecha_final_dt.strftime('%d/%m/%Y')
        eventos = eventos.filter(fecha_final__lte=fecha_final_dt)

    total_eventos = eventos.count()
    total_capacidad = sum(evento.capacidad for evento in eventos)
    total_ingresos = sum(evento.ingresos for evento in eventos)

    data = {
        'eventos': eventos,
        'total_eventos': total_eventos,
        'total_capacidad': total_capacidad,
        'total_ingresos': total_ingresos,
        'hoteles': hoteles,
        'hotel_id': hotel_id,
        'fecha_inicio': fecha_inicio,
        'fecha_final': fecha_final,
    }
    return render(request, 'aplicacion/informe_eventos.html', data)

def informe_servicios(request):
    hoteles = Hotel.objects.all()
    servicios = Servicio.objects.select_related('hotel', 'tipo_servicio').all()

    # Obtener parámetros de filtrado
    hotel_id = request.GET.get('hotel')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_final = request.GET.get('fecha_final')

    # Aplicar filtros
    if hotel_id:
        servicios = servicios.filter(hotel_id=hotel_id)
    if fecha_inicio:
        fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        servicios = servicios.filter(servicio__hotel__reserva__fecha_inicio__gte=fecha_inicio_dt)
    if fecha_final:
        fecha_final_dt = datetime.strptime(fecha_final, '%Y-%m-%d')
        servicios = servicios.filter(servicio__hotel__reserva__fecha_final__lte=fecha_final_dt)

    total_servicios = servicios.count()
    total_valor = sum(servicio.valor for servicio in servicios)

    data = {
        'servicios': servicios,
        'total_servicios': total_servicios,
        'total_valor': total_valor,
        'hoteles': hoteles,
        'hotel_id': hotel_id,
        'fecha_inicio': fecha_inicio,
        'fecha_final': fecha_final,
    }
    return render(request, 'aplicacion/informe_servicios.html', data)