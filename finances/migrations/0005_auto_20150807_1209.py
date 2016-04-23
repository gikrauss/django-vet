# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0004_auto_20150731_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('cant', models.IntegerField(max_length=3, verbose_name=b'cantidad')),
                ('provider', models.ForeignKey(related_name=b'buys', to='finances.Provider')),
            ],
            options={
                'verbose_name': 'compra',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name': 'venta'},
        ),
        migrations.AlterField(
            model_name='sales',
            name='client',
            field=models.ForeignKey(related_name=b'sells', to='clinic.Client'),
        ),
    ]
