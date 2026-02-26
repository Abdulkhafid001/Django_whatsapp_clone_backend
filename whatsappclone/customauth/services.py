from django.contrib.auth import get_user_model
from django.http import JsonResponse
user_model = get_user_model()


def get_all_users():
    queryset = user_model.objects.all().values('username')
    users = list(queryset)
    return users
