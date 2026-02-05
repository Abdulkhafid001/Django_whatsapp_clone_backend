from django.urls import path
from customauth.views import *
urlpatterns = [
    path('', ApiOverview, name='home'),
    path('users/', get_all_users, name='getallusers'),
    path('createuser/', create_user, name='createuser'),
    path('user/<int:id>/', get_user_by_id, name='getuser'),
    path('user/<int:id>/delete/', delete_user, name='deleteuser')
]
