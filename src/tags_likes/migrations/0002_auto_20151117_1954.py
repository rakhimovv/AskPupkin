# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='question',
            field=models.ForeignKey(related_name='likes', default=b'', to='questions.Question'),
        ),
        migrations.AlterField(
            model_name='like',
            name='response',
            field=models.ForeignKey(related_name='likes', default=b'', to='questions.Response'),
        ),
    ]
