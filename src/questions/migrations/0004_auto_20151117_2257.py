# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20151117_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='response',
            name='author',
            field=models.ForeignKey(related_name='responses', to=settings.AUTH_USER_MODEL),
        ),
    ]
