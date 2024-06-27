from django.urls import path
from . import views

urlpatterns = [
    path('', views.tipo_servicio_list, name='tipo_servicio_list'),
    path('nuevo/', views.tipo_servicio_create, name='tipo_servicio_create'),
    path('editar/<int:id>/', views.tipo_servicio_update, name='tipo_servicio_update'),
    path('eliminar/<int:id>/', views.tipo_servicio_delete, name='tipo_servicio_delete'),
]
