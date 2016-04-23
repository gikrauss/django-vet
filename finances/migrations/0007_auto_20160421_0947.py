# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0006_auto_20160419_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='contact',
            field=models.CharField(max_length=200, null=True, verbose_name=b'contacto', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='cat',
            field=models.CharField(max_length=1, verbose_name=b'categoria', choices=[(b'S', b'Servicio'), (b'P', b'Producto'), (b'V', b'Vacuna')]),
        ),
        migrations.AlterField(
            model_name='provider',
            name='phone',
            field=models.CharField(max_length=200, verbose_name=b'telefono'),
        ),
    ]
