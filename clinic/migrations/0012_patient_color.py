# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0011_auto_20160419_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='color',
            field=models.CharField(max_length=200, null=True, verbose_name=b'pelaje', blank=True),
            preserve_default=True,
        ),
    ]
