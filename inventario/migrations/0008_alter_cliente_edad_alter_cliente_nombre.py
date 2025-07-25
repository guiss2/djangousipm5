# Generated by Django 5.2.3 on 2025-07-13 21:28

import inventario.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_cliente_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.PositiveIntegerField(validators=[inventario.validators.validar_edad]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, validators=[inventario.validators.validar_nombre_no_numerico]),
        ),
    ]
