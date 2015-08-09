# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupSpace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('creator', models.CharField(max_length=30, null=True, blank=True)),
                ('createTime', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Group_Relation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remove', models.BooleanField(default=False)),
                ('group', models.ForeignKey(to='workspace.GroupSpace')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSpace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('sex', models.CharField(max_length=10, null=True, blank=True)),
                ('birth', models.DateField(null=True, blank=True)),
                ('highSchool', models.TextField(null=True, blank=True)),
                ('college', models.TextField(null=True, blank=True)),
                ('qq', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('major', models.CharField(max_length=64, null=True, blank=True)),
                ('company', models.CharField(max_length=64, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user_group_relation',
            name='user',
            field=models.ForeignKey(to='workspace.UserSpace'),
            preserve_default=True,
        ),
    ]
