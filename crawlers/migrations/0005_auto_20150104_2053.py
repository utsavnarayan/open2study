# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0004_auto_20150104_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='full_summary',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='instructor',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='summary',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='syllabus',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
