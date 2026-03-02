from django.http import HttpResponse
from django.urls import path
from chat.views import *
urlpatterns = [
    path('', welcome_view),
]
