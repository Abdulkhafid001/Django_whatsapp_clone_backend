from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RegisterViewset

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterViewset.as_view(), name='register')
]
