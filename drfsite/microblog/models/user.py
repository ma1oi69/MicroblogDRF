from django.contrib.auth.models import AbstractUser
from django.db import models
from .properties import choices_country


class CustomUser(AbstractUser):
    sex = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='media/', blank=True)
    country = models.CharField(choices=choices_country, max_length=30)
    age = models.IntegerField(default=0)
    date_of_birthday = models.DateTimeField()
    about = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)


    
