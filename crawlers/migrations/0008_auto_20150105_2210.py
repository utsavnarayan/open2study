# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0007_coursedetails_short_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedetails',
            name='short_url',
        ),
        migrations.AddField(
            model_name='course',
            name='short_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursedetails',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
