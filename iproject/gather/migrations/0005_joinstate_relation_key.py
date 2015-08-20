# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_auto_20150811_2203'),
        ('gather', '0004_auto_20150812_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinstate',
            name='relation_key',
            field=models.ForeignKey(default=1, to='workspace.User_Group_Relation'),
        ),
    ]
