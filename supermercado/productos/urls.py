from django.urls import path
from .views import listar_productos, agregar_producto

urlpatterns = [
    path('', listar_productos, name='listar_productos'),
    path('agregar/', agregar_producto, name='agregar_producto'),
]