# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_auto_20150729_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='temp',
            field=models.CharField(max_length=6, null=True, verbose_name=b'temp', blank=True),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='number_type',
            field=models.CharField(max_length=1, verbose_name=b'tipo', choices=[(b'Celular', b'Celular'), (b'Fijo', b'Fijo'), (b'Trabajo', b'Trabajo')]),
        ),
    ]
