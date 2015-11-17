# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('tags_likes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='tags_likes.Tag'),
        ),
    ]
