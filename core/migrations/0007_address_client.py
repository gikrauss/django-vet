# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20141013_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='client',
            field=models.ForeignKey(default=None, to='core.Client'),
            preserve_default=False,
        ),
    ]
