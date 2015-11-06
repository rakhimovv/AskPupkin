# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='rating',
        ),
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
