from django.shortcuts import render, redirect
from .forms import ProductoForm,RegistroUserForm
from .models import Producto
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'pazYflora/index.html')

def mision(request):
    return render(request, 'pazYflora/mision.html')

def crear(request):
    if request.method =="POST":
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save() #similar en funcion al metodo insert
            return redirect ('index')
    else:
        productoform=ProductoForm()
    return render(request, 'pazYflora/crear.html', {'productoform' : productoform})

def galeria(request):
    productos=Producto.objects.all()
    datos={
        'productos':productos
    }
    return render(request,'pazYflora/galeria.html', datos)    
    # return render(request, 'pazYflora/crear.html')

def productos(request):
    productos=Producto.objects.raw('select * from pazYflora_producto')
    datos={'productos':productos}
    return render(request, 'pazYflora/productos.html', datos)


@login_required
def eliminar(request, id):
    productoEliminado=Producto.objects.get(codigoID=id) #buscamos un vehiculo por la patentes
    productoEliminado.delete()
    return redirect('productos')

@login_required
def modificar(request,id):
    productoModificado = Producto.objects.get(codigoID=id)
    datos ={
        'form': ProductoForm(instance=productoModificado)   #el objeto form llega al template
    }
    if request.method=="POST":          #modificamos backend con los cambios realizados
        formulario = ProductoForm(data=request.POST, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('pazYflora/index.html')
    return render(request,'pazYflora/modificar.html', datos)


