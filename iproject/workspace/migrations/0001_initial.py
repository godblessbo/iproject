# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSpace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('sex', models.CharField(max_length=10, null=True)),
                ('birth', models.DateField(null=True)),
                ('highSchool', models.TextField(null=True)),
                ('college', models.TextField(null=True)),
                ('qq', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('note', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
