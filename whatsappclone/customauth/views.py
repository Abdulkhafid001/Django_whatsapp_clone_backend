from rest_framework import status
from rest_framework import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WcUser
from .serializers import WcUserSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'get_all_users': '/',
        'Search by Username': '/?username=username',
        'Create': '/create',
        'Update': 'update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)


@api_view(['GET'])
def get_all_users(request):
    users = WcUser.objects.all()
    serializer = WcUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = WcUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


def hello(request):
    return HttpResponse('Start implement auth')


def sign_up_brute(request):
    pass
