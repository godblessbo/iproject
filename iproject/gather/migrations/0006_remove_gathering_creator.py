# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0005_joinstate_relation_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gathering',
            name='creator',
        ),
    ]
