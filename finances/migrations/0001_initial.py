# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'nombre producto')),
                ('cost', models.CharField(max_length=200, verbose_name=b'costo')),
                ('price', models.CharField(max_length=200, verbose_name=b'precio')),
                ('stock', models.IntegerField(max_length=200, verbose_name=b'stock')),
                ('cat', models.CharField(max_length=1, verbose_name=b'categoria', choices=[(b'S', b'Servicio'), (b'P', b'Producto')])),
            ],
            options={
                'verbose_name': 'producto',
            },
            bases=(models.Model,),
        ),
    ]
