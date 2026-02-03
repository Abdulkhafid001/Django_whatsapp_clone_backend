from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("chat/", include('chat.urls')),
    path("auth/", include('auth.urls')),
    path('admin/', admin.site.urls),
]
