# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='breed',
            name='specie',
            field=models.ForeignKey(to='core.Specie'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='lastname',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='birthday',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='breed',
            field=models.ForeignKey(to='core.Breed', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.ForeignKey(to='core.Gender', null=True),
            preserve_default=True,
        ),
    ]
