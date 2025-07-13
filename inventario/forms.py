from django import forms
from .models import Producto
from .models import Cliente
from .models import Venta

class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'edad']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'monto', 'fecha']