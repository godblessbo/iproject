# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gathermember',
            name='gatherkey',
        ),
        migrations.AlterField(
            model_name='gathering',
            name='groupkey',
            field=models.ForeignKey(to='workspace.User_Group_Relation'),
        ),
        migrations.DeleteModel(
            name='GatherMember',
        ),
    ]
