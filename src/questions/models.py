from django.db import models
from django.core import urlresolvers
import users
import tags_likes

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey('users.User', related_name='questions')

    tags = models.ManyToManyField('tags_likes.Tag', related_name='questions')

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

    author = models.ForeignKey('users.User', related_name='responses')

    def __unicode__(self):
        return self.content

    class Meta:
        ordering = ['-creation_date']
