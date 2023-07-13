from django.shortcuts import render, redirect
from .forms import ProductoForm,RegistroUserForm
from .models import Producto, Boleta, DetalleBoleta, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from pazYflora.compra import Carrito

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def compras(request):
#     return render(request, 'compras.html')

def mision(request):
    return render(request, 'mision.html')


def galeria(request):
    productos=Producto.objects.all()
    datos={
        'productos':productos
    }
    return render(request,'galeria.html', datos)    

def productos(request):
    productos=Producto.objects.raw('select * from pazYflora_producto')
    datos={'productos':productos}
    return render(request, 'productos.html', datos)

def compras(request):
    compras=Boleta.objects.raw('select * from pazYflora_boleta')
    datos={'boletas':compras}
    return render(request, 'compras.html', datos)


@login_required
def eliminar(request, id):
    productoEliminado=Producto.objects.get(codigoID=id) #buscamos un vehiculo por la patentes
    productoEliminado.delete()
    return redirect('productos')

def crear(request):
    if request.method =="POST":
        productoform = ProductoForm(request.POST, request.FILES)
        
        if productoform.is_valid():
            productoform.save() #similar en funcion al metodo insert
            return redirect ('index')
    else:
        productoform=ProductoForm()
    return render(request, 'crear.html', {'productoform' : productoform})

@login_required
def modificar(request,id):
    productoModificado = Producto.objects.get(codigoID=id)
    datos ={
        'form': ProductoForm(instance=productoModificado)   #el objeto form llega al template
    }
    
    if request.method=="POST":          #modificamos backend con los cambios realizados
        form = ProductoForm(request.POST, request.FILES, instance=productoModificado)
        if form.is_valid():
            form.save()           #modificamos el objeto
            return redirect('productos')
    return render(request,'modificar.html', datos)


def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        userform=RegistroUserForm(data=request.POST)
        #if userform.
        if userform.is_valid():
            userform.save()
            user=authenticate(username=userform.cleaned_data["username"], password=userform.cleaned_data["password1"])
            login(request,user)
            return redirect('index')
        data["form"]=userform
    return render(request,'registration/registrar.html', data)


 
# Administració de Carrito

def agregar_producto(request,id,):
    if request.user.is_authenticated:
        carrito_compra= Carrito(request)
        producto = Producto.objects.get(codigoID=id)
        carrito_compra.agregar(producto=producto)
        return redirect('galeria')
    else:
        return redirect('login')
        

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigoID=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('galeria')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigoID=id)
    carrito_compra.restar(producto=producto)
    return redirect('galeria')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('galeria')    

# FIN Administració de Carrito

def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total, user = request.user.username)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(codigoID = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = DetalleBoleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal, user = request.user.username)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()

    for producto in productos:
        productoModificado = Producto.objects.get(codigoID = producto.id_producto)
        productoModificado.stock = productoModificado.stock - producto.cantidad 
        productoModificado.save()
    

    return render(request, 'index.html',datos)
    # return render(request, 'detallecarrito.html',datos)