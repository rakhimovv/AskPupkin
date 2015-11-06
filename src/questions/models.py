from django.db import models
from django.core import urlresolvers
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, related_name='ask_user')
    avatar = models.ImageField(upload_to='users_avatars')

    def get_absolute_url(self):
        return urlresolvers.reverse('profile', kwargs={'pk': self.pk})


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('User', related_name='questions')
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='questions')

    def get_absolute_url(self):
        return urlresolvers.reverse('question', kwargs={'pk': self.pk})


class Response(models.Model):
    text = models.TextField()
    author = models.ForeignKey('User', related_name='responses')
    question = models.ForeignKey('Question', related_name='responses')
    is_right = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    text = models.CharField(max_length=100, unique=True)


class Like(models.Model):
    user = models.ForeignKey('User', related_name='likes')
    question = models.ForeignKey('Question', related_name='likes')
