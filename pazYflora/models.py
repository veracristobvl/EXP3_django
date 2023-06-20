from tabnanny import verbose
from django.db import models

# Create your models here.
class Producto(models.Model):
    codigoID = models.CharField(primary_key=True, max_length=10, verbose_name="codigoID")
    marca=models.CharField(max_length=50, blank=True, verbose_name="Marca")
    descripcion=models.CharField(max_length=100, blank=True, verbose_name="Descripcion")
    imagen=models.ImageField(upload_to="imagenes",null=True, blank=True,verbose_name="Imagen")
    precio=models.IntegerField(verbose_name="Precio")
    stock=models.IntegerField(verbose_name="Stock")

    def __str__(self):
        return self.codigoID
