from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, blank=True)
    gid = models.CharField(max_length=45, blank=False)