from django.http import HttpResponse
from django.urls import path
from chat.views import *
urlpatterns = [
    path('chat/', welcome_view),
    path('chat/posts/', get_all_blog_posts),
]
