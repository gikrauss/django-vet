# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_auto_20150730_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vac_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'tipo de vacuna')),
            ],
            options={
                'verbose_name': 'tipo de vacuna',
                'verbose_name_plural': 'tipos de vacunas',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='number_type',
            field=models.CharField(max_length=1, verbose_name=b'tipo', choices=[(b'C', b'Celular'), (b'F', b'Fijo'), (b'W', b'Trabajo')]),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='next_vac',
            field=models.ForeignKey(verbose_name=b'pr\xc3\xb3xima vacuna', to='clinic.Vac_Type'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='patient',
            field=models.ForeignKey(related_name=b'vaccine', to='clinic.Patient'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='vac_type',
            field=models.ForeignKey(related_name=b'vac_type', to='clinic.Vac_Type'),
        ),
    ]
