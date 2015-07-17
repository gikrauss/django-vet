# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150716_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='neutered',
            field=models.BooleanField(default=False, verbose_name=b'castrado'),
            preserve_default=True,
        ),
    ]
