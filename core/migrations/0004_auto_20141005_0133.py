# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141005_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'fecha'),
        ),
    ]
