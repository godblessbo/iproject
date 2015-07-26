# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
        ('issue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskspace',
            field=models.ForeignKey(to='workspace.WorkSpace', null=True),
            preserve_default=True,
        ),
    ]
