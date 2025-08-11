from urllib import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_custom_user(request):
    customuser = CustomUserSerializer(data=request.data)
    # validate for already existing data
    if CustomUser.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if customuser.is_valid():
        customuser.save()
        return Response(customuser.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_custom_users(request):
    # checking for the parameters from the URL
    user = CustomUser.objects.all()
    if request.query_params:
        user = CustomUser.objects.filter(**request.query_params.dict())
    # if there is something in items else raise error
    if user:
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
