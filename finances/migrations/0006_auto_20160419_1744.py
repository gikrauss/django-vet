# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_auto_20150807_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='item',
            field=models.ForeignKey(related_name=b'item', verbose_name=b'producto', to='finances.Item'),
        ),
    ]
