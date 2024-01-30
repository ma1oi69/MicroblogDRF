from django.db import models


class Follower(models.Model):
    followers = models.ManyToManyField('CustomUser', related_name='subscribers', blank=True)
    subscriptions = models.ManyToManyField('CustomUser', related_name='followings', blank=True)
