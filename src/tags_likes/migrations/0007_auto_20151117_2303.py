# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_likes', '0006_auto_20151117_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(related_name='likes', to='users.MyUser'),
        ),
    ]
