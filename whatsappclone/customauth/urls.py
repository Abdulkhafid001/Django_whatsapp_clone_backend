from django.urls import path
from customauth.views import *
urlpatterns = [
    path('', ApiOverview, name='home'),
    path('getallusers/', get_all_users, name='getallusers'),
    path('createuser/', create_user, name='createuser')
]
