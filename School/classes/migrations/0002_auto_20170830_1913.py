# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='description',
            field=models.TextField(null=True, verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='name',
            field=models.CharField(max_length=32, verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
