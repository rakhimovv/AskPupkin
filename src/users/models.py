from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.core import urlresolvers


class User(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True)
    USERNAME_FIELD = 'username'
    avatar = models.ImageField(upload_to='users_avatars')

    def get_absolute_url(self):
        return urlresolvers.reverse('profile', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.username
