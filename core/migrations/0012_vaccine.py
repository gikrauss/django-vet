# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_patient_neutered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vac_type', models.CharField(max_length=1, verbose_name=b'tipo', choices=[(b'Q', b'Quintuple'), (b'S', b'Sextuple'), (b'R', b'Rabia'), (b'T', b'Tos de las perreras')])),
                ('marca', models.CharField(max_length=10, verbose_name=b'marca')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha de vacunaci\xc3\xb3n')),
                ('expire_date', models.DateField(verbose_name=b'fecha de vencimiento')),
                ('patient', models.ForeignKey(to='core.Patient')),
            ],
            options={
                'verbose_name': 'Vacunas',
            },
            bases=(models.Model,),
        ),
    ]
