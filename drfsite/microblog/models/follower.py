from django.db import models
from .user import CustomUser


class Follower(models.Model):
    followers = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followers')
    subscriptions = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscribers')
