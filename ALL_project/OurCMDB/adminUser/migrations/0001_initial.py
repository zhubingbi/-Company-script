# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('phone', models.CharField(max_length=16, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7')),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'upload_imgs/')),
            ],
        ),
    ]
