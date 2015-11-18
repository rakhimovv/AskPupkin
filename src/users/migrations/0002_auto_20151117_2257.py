# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20151117_2257'),
        ('tags_likes', '0006_auto_20151117_2257'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=254)),
                ('avatar', models.ImageField(upload_to='users_avatars')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
