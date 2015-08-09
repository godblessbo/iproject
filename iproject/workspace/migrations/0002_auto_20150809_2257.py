# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_group_relation',
            name='isjoin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_group_relation',
            name='reason',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userspace',
            name='homeaddr',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userspace',
            name='loginUser',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userspace',
            name='phone',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userspace',
            name='college',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userspace',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userspace',
            name='highSchool',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
