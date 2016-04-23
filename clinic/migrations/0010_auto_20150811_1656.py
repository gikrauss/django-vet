# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0009_auto_20150804_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breed',
            options={'ordering': ['name'], 'verbose_name': 'raza'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['lastname'], 'verbose_name': 'cliente'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['name'], 'verbose_name': 'paciente'},
        ),
        migrations.AlterModelOptions(
            name='specie',
            options={'ordering': ['name'], 'verbose_name': 'especie'},
        ),
        migrations.AlterModelOptions(
            name='vac_type',
            options={'ordering': ['name'], 'verbose_name': 'tipo de vacuna', 'verbose_name_plural': 'tipos de vacunas'},
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='fc',
            field=models.CharField(max_length=6, null=True, verbose_name=b'fc', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='fr',
            field=models.CharField(max_length=6, null=True, verbose_name=b'fr', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='motive',
            field=models.TextField(null=True, verbose_name=b'motivo de consulta', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='tllc',
            field=models.CharField(max_length=6, null=True, verbose_name=b'tllc', blank=True),
            preserve_default=True,
        ),
    ]
