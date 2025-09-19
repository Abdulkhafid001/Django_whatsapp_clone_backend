from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from core.managers import CustomUserManager


class CustomUser(AbstractUser):
    name = models.CharField(unique=True)
    password = models.CharField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
