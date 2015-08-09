# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gathering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator', models.CharField(max_length=50, null=True, blank=True)),
                ('desp', models.TextField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('startTime', models.DateTimeField(null=True, blank=True)),
                ('endTime', models.DateTimeField(null=True, blank=True)),
                ('place', models.CharField(max_length=128, null=True, blank=True)),
                ('eat', models.CharField(max_length=128, null=True, blank=True)),
                ('sleep', models.CharField(max_length=128, null=True, blank=True)),
                ('budget', models.PositiveIntegerField(null=True, blank=True)),
                ('summary', models.TextField(null=True, blank=True)),
                ('groupkey', models.ForeignKey(to='workspace.GroupSpace')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GatherMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isjoin', models.BooleanField(default=False)),
                ('reason', models.TextField(null=True, blank=True)),
                ('gatherkey', models.ForeignKey(to='gather.Gathering')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
