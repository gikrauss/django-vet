# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_auto_20150731_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complementary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'complementario')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('description', models.TextField(null=True, verbose_name=b'descripci\xc3\xb3n', blank=True)),
                ('attached', models.FileField(upload_to=b'attach/complementary', null=True, verbose_name=b'adjunto', blank=True)),
                ('patient', models.ForeignKey(related_name=b'complementary', to='clinic.Patient')),
            ],
            options={
                'verbose_name': 'Metodo Complementario',
                'verbose_name_plural': 'Metodos Complementarios',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='marca',
            field=models.CharField(max_length=20, verbose_name=b'marca'),
        ),
    ]
