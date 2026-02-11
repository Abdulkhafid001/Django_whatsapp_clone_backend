from django.urls import path
from customauth.views import *
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.tokens import AccessToken
urlpatterns = [
    path('', ApiOverview, name='home'),
    path('users/', get_all_users, name='getallusers'),
    path('createuser/', create_user, name='createuser'),
    path('login/', login, name='loginuser'),
    path('user/<int:id>/', get_user_by_id, name='getuserbyid'),
    path('user/<str:username>/', get_user_by_username, name='getuserbyusername'),
    path('user/<int:id>/delete/', delete_user, name='deleteuser')
]

# JWT paths
urlpatterns += [path('token/', jwt_views.TokenObtainPairView.as_view(), name='Tokenobtainpair'),
                path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),]
