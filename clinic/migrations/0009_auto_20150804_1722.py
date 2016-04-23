# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_auto_20150803_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'An\xc3\xa1lisis Sanguineo')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('description', models.TextField(null=True, verbose_name=b'descripci\xc3\xb3n', blank=True)),
                ('attached', models.FileField(upload_to=b'attach/complementary', null=True, verbose_name=b'adjunto', blank=True)),
                ('patient', models.ForeignKey(related_name=b'analysis', to='clinic.Patient')),
            ],
            options={
                'verbose_name': 'An\xe1lisis Sanguineo',
                'verbose_name_plural': 'An\xe1lisis Sanguineos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deworming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('name', models.CharField(max_length=200, verbose_name=b'antiparasitario')),
                ('patient', models.ForeignKey(related_name=b'deworming', to='clinic.Patient')),
            ],
            options={
                'verbose_name': 'Antiparasitario',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='vac_type',
            field=models.ForeignKey(related_name=b'tipo vacuna', to='clinic.Vac_Type'),
        ),
    ]
