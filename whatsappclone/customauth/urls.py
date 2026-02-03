from django.urls import path
from customauth.views import *
urlpatterns = [
    path('', hello)
]
