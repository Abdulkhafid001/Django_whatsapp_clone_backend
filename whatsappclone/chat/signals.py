from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, PostNotification


@receiver(post_save, sender=Post)
def create_post_notification(sender, instance, created, **kwargs):
    if created:
        PostNotification.objects.create(post=instance, authorName=instance.author)
