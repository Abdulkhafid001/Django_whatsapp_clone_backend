from django.db import models
from django.conf import settings
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'


class Post(models.Model):
    author = models.CharField(null=True)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=2)

    def __str__(self):
        return f'{self.author} published this blog post'
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class PostNotification(models.Model):
    post = models.ForeignKey('Post', null=True, on_delete=models.CASCADE)
    authorName = models.CharField(null=True)


    def __str__(self):
        return f'{self.authorName} published this blog post'
