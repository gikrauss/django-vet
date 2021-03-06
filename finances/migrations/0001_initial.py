# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 21:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('cant', models.IntegerField(verbose_name=b'cantidad')),
                ('pay_type', models.CharField(choices=[(b'E', b'Efectivo'), (b'T', b'Tarjeta'), (b'Ch', b'Cheque'), (b'CC', b'Cuenta Corriente')], max_length=1, null=True, verbose_name=b'forma de pago')),
            ],
            options={
                'verbose_name': 'compra',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'nombre producto')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name=b'costo')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name=b'precio')),
                ('stock', models.IntegerField(verbose_name=b'stock')),
                ('cat', models.CharField(choices=[(b'S', b'Servicio'), (b'P', b'Producto'), (b'V', b'Vacuna')], max_length=1, verbose_name=b'categoria')),
            ],
            options={
                'verbose_name': 'producto',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'proveedor')),
                ('phone', models.CharField(max_length=200, verbose_name=b'telefono')),
                ('email', models.EmailField(max_length=200, verbose_name=b'email')),
                ('contact', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'contacto')),
            ],
            options={
                'verbose_name': 'proveedor',
                'verbose_name_plural': 'proveedores',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('cant', models.IntegerField(verbose_name=b'cantidad')),
                ('pay_type', models.CharField(choices=[(b'E', b'Efectivo'), (b'T', b'Tarjeta'), (b'Ch', b'Cheque'), (b'CC', b'Cuenta Corriente')], max_length=1, null=True, verbose_name=b'forma de pago')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sells', to='clinic.Client')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='finances.Item', verbose_name=b'producto')),
            ],
            options={
                'verbose_name': 'venta',
            },
        ),
        migrations.AddField(
            model_name='buy',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='finances.Item', verbose_name=b'producto'),
        ),
        migrations.AddField(
            model_name='buy',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='finances.Provider'),
        ),
    ]
