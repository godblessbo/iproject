# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0006_remove_gathering_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gathering',
            old_name='group_key',
            new_name='group',
        ),
    ]
