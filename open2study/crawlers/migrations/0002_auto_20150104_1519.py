# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='full_summary',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='summary',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='syllabus',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
