from django.http import HttpResponse
from django.urls import path
from chat.views import *
urlpatterns = [
    path('', welcome_view),
    path('posts/', get_all_blog_posts),
]
