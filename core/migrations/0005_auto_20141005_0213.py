# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141005_0133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breed',
            options={'verbose_name': 'raza'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'cliente'},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name': 'sexo'},
        ),
        migrations.AlterModelOptions(
            name='medicalrecord',
            options={'verbose_name': 'historia cl\xednica'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'paciente'},
        ),
        migrations.AlterModelOptions(
            name='specie',
            options={'verbose_name': 'especie'},
        ),
        migrations.AddField(
            model_name='patient',
            name='specie',
            field=models.ForeignKey(verbose_name=b'especie', to='core.Specie', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='anamnesis',
            field=models.TextField(null=True, verbose_name=b'anamnesis', blank=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='diagnostic',
            field=models.TextField(null=True, verbose_name=b'diagn\xc3\xb3stico', blank=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='exam',
            field=models.TextField(null=True, verbose_name=b'examen', blank=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='ttd',
            field=models.TextField(null=True, verbose_name=b'ttd', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='breed',
            field=smart_selects.db_fields.ChainedForeignKey(verbose_name=b'raza', to='core.Breed', null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='identifier',
            field=models.CharField(max_length=200, null=True, verbose_name=b'identificador', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='initial_anamnesis',
            field=models.TextField(null=True, verbose_name=b'anamnesis', blank=True),
        ),
    ]
