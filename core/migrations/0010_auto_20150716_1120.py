# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150716_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='initial_anamnesis',
            field=models.TextField(null=True, verbose_name=b'anamnesis inicial', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.CharField(max_length=10, null=True, verbose_name=b'peso', blank=True),
        ),
    ]
