# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('questions', '0002_auto_20151118_2341'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags_likes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='responselike',
            name='user',
            field=models.ForeignKey(related_name='r_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questionlike',
            name='question',
            field=models.ForeignKey(related_name='q_likes', blank=True, to='questions.Question', null=True),
        ),
        migrations.AddField(
            model_name='questionlike',
            name='user',
            field=models.ForeignKey(related_name='q_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
