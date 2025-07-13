from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 2 !=0:
        #raise ValidationError('El par debe se par')
        raise ValidationError('%(value)s no es un número par', params={'value': value})
def validar_nombre(value):
    if value == "Comida":
        raise ValidationError('%(value)s no es un texto permitido',
                              params={"value": value})
