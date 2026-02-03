from django.db import models

# Create your models here.


class WcUser(models.Model):
    username = models.TextField(unique=True, max_length=55)
    password = models.TextField(max_length=8)
