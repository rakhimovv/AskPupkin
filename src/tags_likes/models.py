from django.db import models
import questions
import users


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-title']


class Like(models.Model):
    user = models.ForeignKey('users.User', related_name='likes')
    question = models.ForeignKey('questions.Question', related_name='likes', blank=True, null=True)
    response = models.ForeignKey('questions.Response', related_name='likes', blank=True, null=True)

    class Meta:
        ordering = ['-user']
