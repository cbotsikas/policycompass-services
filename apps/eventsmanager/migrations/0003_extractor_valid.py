# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventsmanager', '0002_extractor'),
    ]

    operations = [
        migrations.AddField(
            model_name='extractor',
            name='valid',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
