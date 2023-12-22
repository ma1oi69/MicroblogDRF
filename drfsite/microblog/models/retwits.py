from django.db import models
from .twits import Twits
from .user import CustomUser


class Retweets(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='retweets')
    tweets_id = models.ForeignKey(Twits, on_delete=models.CASCADE, related_name='retweets')
    created_at = models.DateTimeField(auto_now_add=True)


