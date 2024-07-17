from django.urls import path, include
from .views import (tipo_servicio_list, tipo_servicio_create, tipo_servicio_update, tipo_servicio_delete,
                    crear_servicio, lista_servicios, eliminar_servicio, editar_servicio, reporte_habitaciones,
                    reporte_servicios, reporte_reservas, reportes, informe_eventos, informe_servicios, informe_ocupacion
                    )
urlpatterns = [
    path('', tipo_servicio_list, name='tipo_servicio_list'),
    path('nuevo/', tipo_servicio_create, name='tipo_servicio_create'),
    path('editar/<int:id>/', tipo_servicio_update, name='tipo_servicio_update'),
    path('eliminar/<int:id>/', tipo_servicio_delete, name='tipo_servicio_delete'),
    path('crear_servicio/', crear_servicio, name='crear_servicio'),
    path('eliminar_servicio/<int:id>/',  eliminar_servicio, name='eliminar_servicio'),
    path('editar_servicio/<int:id>/', editar_servicio, name='editar_servicio'),
    path('lista_servicios/', lista_servicios, name='lista_servicios'),
    path('reporte_habitaciones/', reporte_habitaciones, name='reporte_habitaciones'),
    path('reporte_servicios/', reporte_servicios, name='reporte_servicios'),
    path('reporte_reservas/', reporte_reservas, name='reporte_reservas'),
    path('reportes/', reportes, name='reportes'),
    path('informe_eventos/', informe_eventos, name='informe_eventos'),
    path('informe_servicios/', informe_servicios, name='informe_servicios'),
    path('informe_ocupacion/', informe_ocupacion, name='informe_ocupacion'),
]
