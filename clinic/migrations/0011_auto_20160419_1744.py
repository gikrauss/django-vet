# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0010_auto_20150811_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='vac_type',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name=b'descripci\xc3\xb3n', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='vac_type',
            field=models.ForeignKey(related_name=b'tipo vacuna', verbose_name=b'tipo de vacuna', to='clinic.Vac_Type'),
        ),
    ]
