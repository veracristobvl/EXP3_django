from django.urls import path
from .views import index, galeria, mision, crear, eliminar, productos, modificar
urlpatterns  = [
    path('', index, name='index'),
    path('productos/', productos, name="productos"),
    path('galeria', galeria, name='galeria'),
    path('mision/', mision, name='mision'),
    path('crear/', crear, name='crear'),
    path('eliminar/<id>', eliminar, name='eliminar'),
    path('modificar/<id>', modificar, name="modificar"),

]