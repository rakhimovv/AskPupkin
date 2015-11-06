# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('is_right', models.BooleanField(default=False)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'users_avatars')),
                ('rating', models.IntegerField()),
                ('user', models.OneToOneField(related_name='ask_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='author',
            field=models.ForeignKey(related_name='responses', to='questions.User'),
        ),
        migrations.AddField(
            model_name='response',
            name='question',
            field=models.ForeignKey(related_name='responses', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(related_name='questions', to='questions.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='questions.Tag'),
        ),
    ]
