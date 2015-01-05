# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0006_auto_20150104_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='short_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
