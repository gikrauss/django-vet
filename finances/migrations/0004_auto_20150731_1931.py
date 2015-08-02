# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_auto_20150718_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'proveedor')),
                ('phone', models.CharField(max_length=20, verbose_name=b'telefono')),
                ('email', models.EmailField(max_length=200, verbose_name=b'email')),
            ],
            options={
                'verbose_name': 'proveedor',
                'verbose_name_plural': 'proveedores',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name': 'compra'},
        ),
    ]
