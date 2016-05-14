# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 21:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name=b'calle y n\xc3\xbamero')),
                ('city', models.CharField(max_length=200, verbose_name=b'ciudad')),
                ('state', models.CharField(choices=[('B', 'Buenos Aires'), ('K', 'Catamarca'), ('H', 'Chaco'), ('U', 'Chubut'), ('C', 'Ciudad Aut\xf3noma de Buenos Aires'), ('X', 'C\xf3rdoba'), ('W', 'Corrientes'), ('E', 'Entre R\xedos'), ('P', 'Formosa'), ('Y', 'Jujuy'), ('L', 'La Pampa'), ('F', 'La Rioja'), ('M', 'Mendoza'), ('N', 'Misiones'), ('Q', 'Neuqu\xe9n'), ('R', 'R\xedo Negro'), ('A', 'Salta'), ('J', 'San Juan'), ('D', 'San Luis'), ('Z', 'Santa Cruz'), ('S', 'Santa Fe'), ('G', 'Santiago del Estero'), ('V', 'Tierra del Fuego, Ant\xe1rtida e Islas del Atl\xe1ntico Sur'), ('T', 'Tucum\xe1n')], max_length=1, verbose_name=b'provincia')),
                ('postal', models.CharField(max_length=6, null=True, verbose_name=b'c\xc3\xb3digo postal')),
            ],
            options={
                'verbose_name': 'direcci\xf3n',
                'verbose_name_plural': 'direcciones',
            },
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'An\xc3\xa1lisis Sanguineo')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('description', models.TextField(blank=True, null=True, verbose_name=b'descripci\xc3\xb3n')),
                ('attached', models.FileField(blank=True, null=True, upload_to=b'attach/complementary', verbose_name=b'adjunto')),
            ],
            options={
                'verbose_name': 'An\xe1lisis Sanguineo',
                'verbose_name_plural': 'An\xe1lisis Sanguineos',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, verbose_name=b'nombre')),
                ('lastname', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'apellido')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name=b'email')),
            ],
            options={
                'ordering': ['lastname'],
                'verbose_name': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Complementary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'complementario')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('description', models.TextField(blank=True, null=True, verbose_name=b'descripci\xc3\xb3n')),
                ('attached', models.FileField(blank=True, null=True, upload_to=b'attach/complementary', verbose_name=b'adjunto')),
            ],
            options={
                'verbose_name': 'Metodo Complementario',
                'verbose_name_plural': 'Metodos Complementarios',
            },
        ),
        migrations.CreateModel(
            name='Deworming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha de desparasitaci\xc3\xb3n')),
                ('name', models.CharField(max_length=200, verbose_name=b'antiparasitario')),
                ('dose', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'posolog\xc3\xada')),
            ],
            options={
                'verbose_name': 'Antiparasitario',
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha')),
                ('motive', models.TextField(blank=True, null=True, verbose_name=b'motivo de consulta')),
                ('temp', models.CharField(blank=True, max_length=6, null=True, verbose_name=b'temp')),
                ('fc', models.CharField(blank=True, max_length=6, null=True, verbose_name=b'fc')),
                ('fr', models.CharField(blank=True, max_length=6, null=True, verbose_name=b'fr')),
                ('tllc', models.CharField(blank=True, max_length=6, null=True, verbose_name=b'tllc')),
                ('anamnesis', models.TextField(blank=True, null=True, verbose_name=b'anamnesis')),
                ('exam', models.TextField(blank=True, null=True, verbose_name=b'examen')),
                ('diagnostic', models.TextField(blank=True, null=True, verbose_name=b'diagn\xc3\xb3stico')),
                ('tto', models.TextField(blank=True, null=True, verbose_name=b'indicaciones')),
                ('attached', models.FileField(blank=True, null=True, upload_to=b'attach/', verbose_name=b'adjunto')),
            ],
            options={
                'verbose_name': 'historia cl\xednica',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'nombre')),
                ('gender', models.CharField(choices=[(b'Macho', b'Macho'), (b'Hembra', b'Hembra')], max_length=6, null=True, verbose_name=b'sexo')),
                ('neutered', models.BooleanField(default=False, verbose_name=b'castrado')),
                ('birthday', models.DateField(null=True, verbose_name=b'fecha de nacimiento')),
                ('weight', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'peso')),
                ('color', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'pelaje')),
                ('identifier', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'identificador')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'patient_photo', verbose_name=b'im\xc3\xa1gen')),
                ('initial_anamnesis', models.TextField(blank=True, null=True, verbose_name=b'anamnesis inicial')),
                ('breed', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field=b'specie', chained_model_field=b'specie', null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.Breed', verbose_name=b'raza')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='clinic.Client', verbose_name=b'due\xc3\xb1o')),
                ('specie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.Specie', verbose_name=b'especie')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'paciente',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, verbose_name=b'n\xc3\xbamero')),
                ('number_type', models.CharField(choices=[(b'C', b'Celular'), (b'F', b'Fijo'), (b'W', b'Trabajo')], max_length=1, verbose_name=b'tipo')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='clinic.Client')),
            ],
            options={
                'verbose_name': 'n\xfamero de tel\xe9fono',
                'verbose_name_plural': 'n\xfameros de tel\xe9fono',
            },
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'fecha de vacunaci\xc3\xb3n')),
                ('marca', models.CharField(max_length=20, verbose_name=b'marca')),
                ('expire_date', models.DateField(verbose_name=b'fecha de vencimiento')),
                ('next_vac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.Vac_Type', verbose_name=b'pr\xc3\xb3xima vacuna')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine', to='clinic.Patient')),
                ('vac_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vac_type', to='settings.Vac_Type', verbose_name=b'tipo de vacuna')),
            ],
            options={
                'verbose_name': 'Vacuna',
            },
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='clinic.Patient'),
        ),
        migrations.AddField(
            model_name='deworming',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deworming', to='clinic.Patient'),
        ),
        migrations.AddField(
            model_name='complementary',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complementary', to='clinic.Patient'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis', to='clinic.Patient'),
        ),
        migrations.AddField(
            model_name='address',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='clinic.Client'),
        ),
    ]
