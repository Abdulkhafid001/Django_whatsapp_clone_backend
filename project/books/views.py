from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer, UserSerializer
from django.contrib.auth.models import User



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RegisterViewset(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer