# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200, verbose_name=b'calle y n\xc3\xbamero')),
                ('city', models.CharField(max_length=200, verbose_name=b'ciudad')),
                ('state', models.CharField(max_length=1, verbose_name=b'provincia', choices=[('B', 'Buenos Aires'), ('K', 'Catamarca'), ('H', 'Chaco'), ('U', 'Chubut'), ('C', 'Ciudad Aut\xf3noma de Buenos Aires'), ('X', 'C\xf3rdoba'), ('W', 'Corrientes'), ('E', 'Entre R\xedos'), ('P', 'Formosa'), ('Y', 'Jujuy'), ('L', 'La Pampa'), ('F', 'La Rioja'), ('M', 'Mendoza'), ('N', 'Misiones'), ('Q', 'Neuqu\xe9n'), ('R', 'R\xedo Negro'), ('A', 'Salta'), ('J', 'San Juan'), ('D', 'San Luis'), ('Z', 'Santa Cruz'), ('S', 'Santa Fe'), ('G', 'Santiago del Estero'), ('V', 'Tierra del Fuego, Ant\xe1rtida e Islas del Atl\xe1ntico Sur'), ('T', 'Tucum\xe1n')])),
                ('postal', models.CharField(max_length=6, null=True, verbose_name=b'c\xc3\xb3digo postal')),
            ],
            options={
                'verbose_name': 'direcci\xf3n',
                'verbose_name_plural': 'direcciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'nombre')),
            ],
            options={
                'verbose_name': 'raza',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=200, verbose_name=b'nombre')),
                ('lastname', models.CharField(max_length=200, null=True, verbose_name=b'apellido', blank=True)),
                ('email', models.EmailField(max_length=200, null=True, verbose_name=b'email', blank=True)),
            ],
            options={
                'verbose_name': 'cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'nombre')),
            ],
            options={
                'verbose_name': 'sexo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('temp', models.CharField(max_length=5, null=True, verbose_name=b'temp', blank=True)),
                ('anamnesis', models.TextField(null=True, verbose_name=b'anamnesis', blank=True)),
                ('exam', models.TextField(null=True, verbose_name=b'examen', blank=True)),
                ('diagnostic', models.TextField(null=True, verbose_name=b'diagn\xc3\xb3stico', blank=True)),
                ('tto', models.TextField(null=True, verbose_name=b'indicaciones', blank=True)),
            ],
            options={
                'verbose_name': 'historia cl\xednica',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'nombre')),
                ('neutered', models.BooleanField(default=False, verbose_name=b'castrado')),
                ('birthday', models.DateField(null=True, verbose_name=b'fecha de nacimiento')),
                ('weight', models.CharField(max_length=10, null=True, verbose_name=b'peso', blank=True)),
                ('identifier', models.CharField(max_length=200, null=True, verbose_name=b'identificador', blank=True)),
                ('initial_anamnesis', models.TextField(null=True, verbose_name=b'anamnesis inicial', blank=True)),
                ('breed', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'specie', chained_field=b'specie', verbose_name=b'raza', auto_choose=True, to='clinic.Breed', null=True)),
                ('gender', models.ForeignKey(verbose_name=b'sexo', to='clinic.Gender', null=True)),
                ('owner', models.ForeignKey(verbose_name=b'due\xc3\xb1o', to='clinic.Client')),
            ],
            options={
                'verbose_name': 'paciente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200, verbose_name=b'n\xc3\xbamero')),
                ('number_type', models.CharField(max_length=1, verbose_name=b'tipo', choices=[(b'C', b'Celular'), (b'F', b'Fijo'), (b'W', b'Trabajo')])),
                ('client', models.ForeignKey(to='clinic.Client')),
            ],
            options={
                'verbose_name': 'n\xfamero de tel\xe9fono',
                'verbose_name_plural': 'n\xfameros de tel\xe9fono',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'nombre')),
            ],
            options={
                'verbose_name': 'especie',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vac_type', models.CharField(max_length=1, verbose_name=b'tipo', choices=[(b'Q', b'Quintuple'), (b'S', b'Sextuple'), (b'R', b'Rabia'), (b'T', b'Tos de las perreras')])),
                ('marca', models.CharField(max_length=10, verbose_name=b'marca')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha de vacunaci\xc3\xb3n')),
                ('expire_date', models.DateField(verbose_name=b'fecha de vencimiento')),
                ('next_vac', models.CharField(max_length=1, null=True, verbose_name=b'pr\xc3\xb3xima vacuna', choices=[(b'Q', b'Quintuple'), (b'S', b'Sextuple'), (b'R', b'Rabia'), (b'T', b'Tos de las perreras')])),
                ('patient', models.ForeignKey(to='clinic.Patient')),
            ],
            options={
                'verbose_name': 'Vacuna',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patient',
            name='specie',
            field=models.ForeignKey(verbose_name=b'especie', to='clinic.Specie', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(to='clinic.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='breed',
            name='specie',
            field=models.ForeignKey(to='clinic.Specie'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='client',
            field=models.ForeignKey(to='clinic.Client'),
            preserve_default=True,
        ),
    ]
