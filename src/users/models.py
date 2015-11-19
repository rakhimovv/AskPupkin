from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import urlresolvers


class User(AbstractUser):
    # username = models.CharField(max_length=254, unique=True)
    # USERNAME_FIELD = 'username'
    avatar = models.ImageField(upload_to='users_avatars', blank=True, null=True)

    def get_absolute_url(self):
        return urlresolvers.reverse('profile', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.username
