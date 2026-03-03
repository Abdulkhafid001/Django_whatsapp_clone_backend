from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome_view),
    path('postnotification/<int:pk>', views.PostNotificationDetailView.as_view())
]
