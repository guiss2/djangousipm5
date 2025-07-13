from django.contrib import admin

# Register your models here.
from .models import Categoria, Cliente, Producto, Venta, Demo


admin.site.register(Categoria)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'disponible', 'created_at', 'updated_at')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('categoria', 'disponible',)

admin.site.register(Producto, ProductoAdmin)
#se registraron los modelos Cliente y Venta
admin.site.register(Cliente)
admin.site.register(Venta)