# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20151117_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(related_name='questions', to='users.MyUser'),
        ),
        migrations.AlterField(
            model_name='response',
            name='author',
            field=models.ForeignKey(related_name='responses', to='users.MyUser'),
        ),
    ]
