# Generated by Django 4.2.21 on 2025-07-25 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0015_ordenventa_moneda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenventa',
            name='moneda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sample.moneda'),
        ),
    ]
