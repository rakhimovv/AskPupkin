from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
import questions
import users


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-title']


class QuestionLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='q_likes')
    question = models.ForeignKey('questions.Question', related_name='q_likes', blank=True, null=True)
    # content_type = models.ForeignKey(ContentType, blank=True, null=True)
    # object_id = models.PositiveIntegerField(blank=True, null=True)
    # content_object = generic.GenericForeignKey('content_type', 'object_id')


class ResponseLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='r_likes')
    response = models.ForeignKey('questions.Response', related_name='r_likes', blank=True, null=True)
