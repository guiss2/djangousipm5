from datetime import date
from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 2 !=0:
        #raise ValidationError('El costo o precio debe se par')
        raise ValidationError('%(value)s no es un número par', params={'value': value})
def validar_nombre(value):
    if value == "Comida":
        raise ValidationError('%(value)s no es un texto permitido',
                              params={"value": value})
        
#validaciones personalizadas para el modelo Cliente
def validar_nombre_no_numerico(value):
    # Validación 1
    if value.isnumeric():
        raise ValidationError('%(value)s: El nombre no puede contener solo números', params={"value": value})

# Validación 2
def validar_edad(value):
    if value < 15:
        raise ValidationError('%(value)s: El cliente debe ser mayor de edad (15+).', params={"value": value})

        
#validaciones para el modelo venta
# Validación 1
def validar_monto_positivo(value):
    if value <= 0:
        raise ValidationError('%(value)s: El monto debe ser mayor que cero.', params={"value": value})

# Validación 2
def validar_fecha_no_futura(value):
    if value > date.today():
        raise ValidationError('%(value)s: La fecha de la venta no puede estar en el futuro.', params={"value": value})
