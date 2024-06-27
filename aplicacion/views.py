from django.shortcuts import render, get_object_or_404, redirect
from .models import TipoServicio, Servicio
from .forms import TipoServicioForm, ServicioForm

def tipo_servicio_list(request):
    servicios = TipoServicio.objects.all()
    return render(request, 'aplicacion/tipo_servicio_list.html', {'servicios': servicios})

def tipo_servicio_create(request):
    if request.method == 'POST':
        form = TipoServicioForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('tipo_servicio_list')
    else:
        form = TipoServicioForm(instance=servicio)
    return render(request, 'aplicacion/tipo_servicio_form.html', {'form': form})

def tipo_servicio_delete(request, id):
    servicio = get_object_or_404(TipoServicio, id=id)
    if request.method == 'POST':
        servicio.delete()
        return redirect('tipo_servicio_list')
    return render(request, 'aplicacion/tipo_servicio_confirm_delete.html', {'servicio': servicio})

def crear_servicio(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('lista_servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'aplicacion/editar_servicio.html', {'form': form, 'servicio': servicio})

def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if request.method == "POST":
        servicio.delete()
        return redirect('lista_servicios') 
    return render(request, 'aplicacion/eliminar_servicio.html', {'servicio': servicio})
