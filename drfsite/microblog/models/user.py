from django.contrib.auth.models import AbstractUser
from django.db import models
from .properties import choices_country
from microblog.models.follower import Follower


class CustomUser(AbstractUser):
    sex = models.CharField(max_length=5)
    country = models.CharField(choices=choices_country, max_length=30)
    age = models.IntegerField(default=0)
    date_of_birthday = models.DateTimeField()
    about = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    subscriptions = models.ManyToManyField(Follower, related_name='user_subscriptions', blank=True)
