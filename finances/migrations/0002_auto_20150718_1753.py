# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('client', models.ForeignKey(to='clinic.Client')),
                ('item', models.ForeignKey(to='finances.Item')),
            ],
            options={
                'verbose_name': 'venta',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.DecimalField(default=0, verbose_name=b'costo', max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(default=0, verbose_name=b'precio', max_digits=12, decimal_places=2),
        ),
    ]
