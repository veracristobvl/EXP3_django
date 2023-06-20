#es una clase que tiene la información que llevará uno o  más formularios en un template
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class RegistroUserForm(UserCreationForm):
    class Meta: 
        model=User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['codigoID', 'marca', 'descripcion','imagen', 'precio','stock']
        labels = {
            'codigoID' : "CodigoID",
            'marca' : "Marca",
            'descripcion' : "Descripcion",
            'imagen': "Imagen",
            'precio': 'Precio',
            'stock':'Stock'
        }
        widgets={
            'codigoID' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese un codigo ID',
                    'class' : 'form-control',
                    'id' : 'codigoID'
                }
            ),
            'marca':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese una marca',
                    'class' : 'form-control',
                    'id' : 'marca'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese una descripcion',
                    'class' : 'form-control',
                    'id' : 'descripcion'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class' : 'form-control',
                    'id' : 'imagen'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                     'placeholder' : 'Ingrese precio',
                     'class' : 'form-control',
                     'id' : 'precio'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'placeholder' : 'Ingrese stock',
                    'class' : 'form-control',
                    'id' : 'stock'
                }
            )
        }