from django.urls import path
from . import views

urlpatterns = [
    path('createuser/', views.create_custom_user, name='create custom users'),
    path('users/', views.get_custom_users, name='view custom users'),
]
