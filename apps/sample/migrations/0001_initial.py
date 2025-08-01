# Generated by Django 4.2.21 on 2025-07-18 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ov', models.CharField(max_length=20, unique=True, verbose_name='Número OV')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha creación')),
                ('hora_creacion', models.TimeField(verbose_name='Hora creación')),
                ('ov_vinculado', models.CharField(blank=True, max_length=20, null=True, verbose_name='O.V. Vinculado')),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto Total')),
                ('destino', models.CharField(max_length=100, verbose_name='Destino')),
                ('canal_ventas', models.CharField(max_length=50, verbose_name='Canal Ventas')),
                ('cantidad_items', models.IntegerField(verbose_name='Cant. Items')),
                ('pickear', models.BooleanField(default=True, verbose_name='Pickear')),
                ('estado_asignacion_lotes', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Terminado', 'Terminado')], max_length=50, verbose_name='Estado Asignación de Lotes')),
                ('estado_sap', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Integrado', 'Integrado'), ('Error', 'Error')], max_length=50, verbose_name='Estado SAP')),
                ('respuesta_integrador', models.TextField(blank=True, null=True, verbose_name='Respuesta de Integrador')),
                ('asesor_comercial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Asesor Comercial')),
            ],
        ),
    ]
