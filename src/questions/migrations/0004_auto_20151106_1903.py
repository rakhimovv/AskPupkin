# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20151105_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='value',
        ),
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
