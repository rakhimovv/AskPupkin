# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_likes', '0002_auto_20151117_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='question',
            field=models.ForeignKey(related_name='likes', to='questions.Question', null=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='response',
            field=models.ForeignKey(related_name='likes', to='questions.Response', null=True),
        ),
    ]
