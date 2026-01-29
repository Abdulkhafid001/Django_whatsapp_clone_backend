from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
