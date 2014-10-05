# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20140930_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'fecha')),
                ('anamnesis', models.TextField(null=True, verbose_name=b'anamnesis')),
                ('exam', models.TextField(null=True, verbose_name=b'examen')),
                ('diagnostic', models.TextField(null=True, verbose_name=b'diagn\xc3\xb3stico')),
                ('ttd', models.TextField(null=True, verbose_name=b'ttd')),
                ('patient', models.ForeignKey(to='core.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patient',
            name='identifier',
            field=models.CharField(max_length=200, null=True, verbose_name=b'identificador'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='initial_anamnesis',
            field=models.TextField(null=True, verbose_name=b'anamnesis inicial'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='breed',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=200, null=True, verbose_name=b'email', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='firstname',
            field=models.CharField(max_length=200, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='client',
            name='lastname',
            field=models.CharField(max_length=200, null=True, verbose_name=b'apellido', blank=True),
        ),
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthday',
            field=models.DateField(null=True, verbose_name=b'fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='breed',
            field=models.ForeignKey(verbose_name=b'raza', to='core.Breed', null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.ForeignKey(verbose_name=b'sexo', to='core.Gender', null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='owner',
            field=models.ForeignKey(verbose_name=b'due\xc3\xb1o', to='core.Client'),
        ),
        migrations.AlterField(
            model_name='specie',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'nombre'),
        ),
    ]
