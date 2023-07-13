#es una clase que tiene la información que llevará uno o  más formularios en un template
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User 


# class RegistroUserForm(UserCreationForm):
#     class Meta: 
#         model=User 
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#         widgets={
#             'first_name' : forms.TextInput(
#                 attrs={
#                     'placeholder' : 'dksjd',
#                     'class' : '',
#                     'id' : 'first_name'
#                 }
#             ),
#             'last_name' : forms.TextInput(
#                 attrs={
#                     'placeholder' : '',
#                     'class' : '',
#                     'id' : 'last_name',
#                     'required': True
#                 }
#             )
#         }
class RegistroUserForm(UserCreationForm):
    class Meta: 
        model=User 
        #fields = ['username', 'nombre', 'apellido', 'email', 'password1', 'password2']
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets={
            'username' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese Nombre de Usuario',
                    'class' : 'form_control',
                    'id' : 'username',
                    'required': True
                }
            ),
            'first_name' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese Nombre',
                    'class' : '',
                    'id' : 'nombre',
                    'required': True
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese Apellido',
                    'class' : '',
                    'id' : 'apellido',
                    'required': True
                }
            ),
            'email' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese Email',
                    'class' : '',
                    'id' : 'email',
                    'required': True
                }
            ),
            'password1' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese Contraseña',
                    'class' : '',
                    'id' : 'password1',
                }
            ),
            'password2' : forms.TextInput(
                attrs={
                    'placeholder' : 'Reingrese Contraseña',
                    'class' : '',
                    'id' : 'password2',
                }
            ),
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de Usuario'
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Reingresa  Contraseña'
        # for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None

class ProductoForm(ModelForm):
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