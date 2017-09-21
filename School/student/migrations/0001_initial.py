# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=8)),
                ('grade', models.CharField(max_length=64)),
                ('teacher', models.ManyToManyField(to='teacher.Teacher')),
            ],
        ),
    ]
