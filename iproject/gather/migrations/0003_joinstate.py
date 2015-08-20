# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_auto_20150811_2203'),
        ('gather', '0002_auto_20150809_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isjoin', models.BooleanField(default=False)),
                ('reason', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
