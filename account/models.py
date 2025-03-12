from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

class User(AbstractUser):
    mobile = models.CharField(max_length=25)
    gid = models.CharField(max_length=45)
    