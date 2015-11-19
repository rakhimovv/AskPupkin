from django.db import models
from django.conf import settings
from django.core import urlresolvers
from django.db.models import Count


class QuestionQuerySet(models.QuerySet):
    def get_popular(self):
        return self.annotate(likes_count=Count('q_likes')).order_by('-likes_count')

    def get_last(self):
        return self.order_by('-creation_date')

    def get_by_tag(self, tag):
        return self.filter(tags__title__contains=tag).order_by('-creation_date')


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions')

    tags = models.ManyToManyField('tags_likes.Tag', related_name='questions')

    objects = QuestionQuerySet.as_manager()

    def get_absolute_url(self):
        return urlresolvers.reverse('question', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-creation_date']


class Response(models.Model):
    content = models.TextField(default='')
    is_right = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey('Question', related_name='responses')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='responses')

    def __unicode__(self):
        return self.content

    class Meta:
        ordering = ['-creation_date']
