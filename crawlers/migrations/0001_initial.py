# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('url', models.URLField()),
                ('name', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instructor', models.TextField()),
                ('summary', models.TextField(max_length=200)),
                ('full_summary', models.TextField(max_length=200)),
                ('syllabus', models.TextField(max_length=200)),
                ('popularity', models.IntegerField(default=0)),
                ('course', models.ForeignKey(to='crawlers.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
