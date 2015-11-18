# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151117_2257'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='User',
        ),
    ]
