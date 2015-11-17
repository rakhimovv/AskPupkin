# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='questions', to='users.User')),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('is_right', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='responses', to='users.User')),
                ('question', models.ForeignKey(related_name='responses', to='questions.Question')),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
    ]
