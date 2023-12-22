from django.db import models

from .twits import Twits


class Comments(models.Model):
    tweet = models.ForeignKey(Twits, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
