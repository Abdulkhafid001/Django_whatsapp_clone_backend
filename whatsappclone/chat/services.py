from chat.models import PostNotification


def get_all_post_notifications():
    queryset = PostNotification.objects.all().values('post', 'authorName')
    post_notifications = list(queryset)
    return post_notifications
