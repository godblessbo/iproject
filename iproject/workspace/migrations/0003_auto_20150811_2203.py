# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_auto_20150809_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_group_relation',
            name='isjoin',
        ),
        migrations.RemoveField(
            model_name='user_group_relation',
            name='reason',
        ),
    ]
