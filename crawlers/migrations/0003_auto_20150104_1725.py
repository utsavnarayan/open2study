# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0002_auto_20150104_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='id',
            new_name='course_id',
        ),
    ]
