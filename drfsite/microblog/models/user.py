from django.contrib.auth.models import AbstractUser
from django.db import models
from .properties import choices_country


class CustomUser(AbstractUser):
    CHOICES_SEX = [('M', 'Men'), ('W', 'Women')]
    sex = models.CharField(choices=CHOICES_SEX, max_length=1)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    country = models.CharField(choices=choices_country, max_length=100)
    age = models.IntegerField(default=0)
    date_of_birthday = models.DateTimeField(auto_now_add=True)
    about = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    
