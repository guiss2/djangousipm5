import uuid
from django.db import models
from .validators import validar_edad, validar_fecha_no_futura, validar_monto_positivo, validar_nombre_no_numerico, validar_par

#MODELO 1
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
#MODELO 2
class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'

#MODELO 3
class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_par])
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS
    )
    disponible = models.BooleanField(blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
#MODELO  4
class Demo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombres = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombres
    
#MODELO 5
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validar_nombre_no_numerico])
    correo = models.EmailField(unique=True)
    edad = models.PositiveIntegerField(validators=[validar_edad])

    def __str__(self):
        return self.nombre
    
#MODELO 6
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    monto = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_monto_positivo])
    fecha = models.DateField(validators=[validar_fecha_no_futura])
    

    def __str__(self):
        return f"Venta a {self.cliente.nombre} - {self.fecha}"