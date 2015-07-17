# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20141013_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='ttd',
        ),
        migrations.AddField(
            model_name='address',
            name='postal',
            field=models.CharField(max_length=6, null=True, verbose_name=b'c\xc3\xb3digo postal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='temp',
            field=models.CharField(max_length=5, null=True, verbose_name=b'temp', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='tto',
            field=models.TextField(null=True, verbose_name=b'indicaciones', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.CharField(max_length=10, null=True, verbose_name=b'peso'),
            preserve_default=True,
        ),
    ]
