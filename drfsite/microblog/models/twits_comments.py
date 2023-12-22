from django.db import models
from .twits import Twits
from .comments import Comments


class TwitsComments(models.Model):
    tweets_id = models.ForeignKey(Twits, on_delete=models.CASCADE, related_name='tweets')
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)