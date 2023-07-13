from tabnanny import verbose
import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
#from django.contrib.auth.models import User


# Create your models here.
class Producto(models.Model):
    codigoID = models.CharField(primary_key=True, max_length=10, verbose_name="codigoID")
    marca = models.CharField(max_length=50, blank=True, verbose_name="Marca")
    descripcion = models.CharField(max_length=100, blank=True, verbose_name="Descripcion")
    imagen = models.ImageField(upload_to="imagenes",null=True, blank=True,verbose_name="Imagen")
    precio = models.IntegerField(verbose_name="Precio" )
    stock = models.IntegerField(verbose_name="Stock")

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=10, verbose_name="Username")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, blank=True, verbose_name="Apellido")
    email = models.CharField(max_length=100, blank=True, verbose_name="Email")
    password1 = models.CharField(max_length=100, blank=True, verbose_name="Password1")
    password2 = models.CharField(max_length=100, blank=True, verbose_name="Password2")
    
    def __str__(self):
        return self.username

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    user = models.CharField(max_length=100, blank=True, verbose_name="Usuario")
    def __str__(self):
        return str(self.id_boleta)

class DetalleBoleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()
    user = models.CharField(max_length=100, blank=True, verbose_name="Usuario")
    def __str__(self):
        return str(self.id_detalle_boleta)