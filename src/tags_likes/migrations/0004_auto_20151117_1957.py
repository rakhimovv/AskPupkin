# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_likes', '0003_auto_20151117_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='question',
            field=models.ForeignKey(related_name='likes', blank=True, to='questions.Question'),
        ),
        migrations.AlterField(
            model_name='like',
            name='response',
            field=models.ForeignKey(related_name='likes', blank=True, to='questions.Response'),
        ),
    ]
