# Generated by Django 4.2.21 on 2025-07-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0013_alter_ordenventa_asesor_comercial_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
