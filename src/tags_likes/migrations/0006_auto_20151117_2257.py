# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tags_likes', '0005_auto_20151117_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
