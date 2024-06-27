from django.urls import path, include
from .views import tipo_servicio_list, tipo_servicio_create, tipo_servicio_update, tipo_servicio_delete

urlpatterns = [
    path('', tipo_servicio_list, name='tipo_servicio_list'),
    path('nuevo/', tipo_servicio_create, name='tipo_servicio_create'),
    path('editar/<int:id>/', tipo_servicio_update, name='tipo_servicio_update'),
    path('eliminar/<int:id>/', tipo_servicio_delete, name='tipo_servicio_delete'),
]
