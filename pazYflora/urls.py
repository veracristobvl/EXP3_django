from django.urls import path
from .views import index, galeria, mision, crear, eliminar, productos, modificar, registrar,generarBoleta, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, compras
urlpatterns  = [
    path('', index, name='index'),
    path('productos/', productos, name="productos"),
    path('crear/', crear, name='crear'),
    path('eliminar/<id>', eliminar, name='eliminar'),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/',registrar,name="registrar"),
    path('galeria', galeria, name='galeria'),
    path('mision/', mision, name='mision'),
    path('compras/', compras, name='compras'),
    
    # Url's de carrito
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    
    ]