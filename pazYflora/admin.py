from django.contrib import admin
from .models import Producto, Boleta, DetalleBoleta, User
# Register your models here.
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)
admin.site.register(User)
