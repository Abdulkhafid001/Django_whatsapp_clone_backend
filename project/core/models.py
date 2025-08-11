from django.db import models
from django.urls import reverse

# Create your models here.


class CustomUser(models.Model):
    name = models.CharField()
    password = models.CharField()
    date_joined = models.DateTimeField(auto_now_add=True)
