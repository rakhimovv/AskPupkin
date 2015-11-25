from django.conf import settings
from django.db import models
import questions


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-title']


class QuestionLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='q_likes')
    question = models.ForeignKey('questions.Question', related_name='q_likes', blank=True, null=True)


class ResponseLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='r_likes')
    response = models.ForeignKey('questions.Response', related_name='r_likes', blank=True, null=True)
