from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('bookapi/', include('books.urls')),
    # JWT Auth Endpoints
    path('bookapi/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('bookapi/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
