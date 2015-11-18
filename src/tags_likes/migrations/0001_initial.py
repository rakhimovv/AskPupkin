# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.ForeignKey(related_name='q_likes', blank=True, to='questions.Question', null=True)),
                ('user', models.ForeignKey(related_name='q_likes', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response', models.ForeignKey(related_name='r_likes', blank=True, to='questions.Response', null=True)),
                ('user', models.ForeignKey(related_name='r_likes', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
    ]
