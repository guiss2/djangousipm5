# Generated by Django 5.2.3 on 2025-07-13 21:43

import inventario.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_alter_cliente_edad_alter_cliente_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=10, validators=[inventario.validators.validar_monto_positivo]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(validators=[inventario.validators.validar_fecha_no_futura]),
        ),
    ]
