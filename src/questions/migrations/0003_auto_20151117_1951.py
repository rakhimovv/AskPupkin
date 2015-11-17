# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='content',
            field=models.TextField(default=b''),
        ),
    ]
