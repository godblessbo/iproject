# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_auto_20150811_2203'),
        ('gather', '0003_joinstate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joinstate',
            old_name='isjoin',
            new_name='isJoin',
        ),
        migrations.RemoveField(
            model_name='gathering',
            name='groupkey',
        ),
        migrations.AddField(
            model_name='gathering',
            name='group_key',
            field=models.ForeignKey(default=1, to='workspace.GroupSpace'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joinstate',
            name='upMoney',
            field=models.BooleanField(default=False),
        ),

    ]
