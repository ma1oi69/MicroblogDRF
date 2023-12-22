from django.db import models
from .user import CustomUser


class Twits(models.Model):
    title = models.CharField(max_length=400)
    like = models.IntegerField(default=0)
    repost = models.IntegerField(default=0)
    answers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, related_name='twits', on_delete=models.CASCADE)
