# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('gender', models.CharField(max_length=32, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('age', models.IntegerField(verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84')),
                ('birthday', models.DateTimeField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5')),
                ('grade', models.CharField(max_length=32, verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7')),
                ('subject', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\x93\xe4\xb8\x9a')),
                ('city', models.CharField(max_length=32, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82')),
            ],
        ),
    ]
