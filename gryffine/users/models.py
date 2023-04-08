from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    telegram_id = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now, null=True, blank=True)