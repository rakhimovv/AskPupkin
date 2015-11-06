# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20151105_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='rating',
        ),
        migrations.AddField(
            model_name='like',
            name='question',
            field=models.ForeignKey(related_name='likes', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(related_name='likes', to='questions.User'),
        ),
    ]
