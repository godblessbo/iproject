# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator', models.CharField(max_length=50, null=True)),
                ('owner', models.CharField(max_length=50, null=True)),
                ('task', models.TextField(null=True)),
                ('process', models.TextField(null=True)),
                ('startTime', models.DateField(null=True)),
                ('endTime', models.DateField(null=True)),
                ('state', models.CharField(default=False, max_length=10, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
