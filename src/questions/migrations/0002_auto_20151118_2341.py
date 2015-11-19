# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
        ('tags_likes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='author',
            field=models.ForeignKey(related_name='responses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='response',
            name='question',
            field=models.ForeignKey(related_name='responses', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='tags_likes.Tag'),
        ),
    ]
