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
        'get_all_users': 'users/',
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


@api_view(['GET'])
def get_user_by_id(request, id):
    wc_user = WcUser.objects.get(id=id)
    if wc_user.__class__.objects.exists():
        serializer = WcUserSerializer(wc_user)
        return Response(serializer.data)
    return Response('User with Id does not exist')


@api_view(['GET'])
def delete_user(request, id):
    user = WcUser.objects.get(id=id)
    serializer = WcUserSerializer(user)
    # print(serializer.data)
    # if serializer.is_valid
    # if request.user.is_authenticated():
    #     if request.user.is_super_user():
    #         if user.is_superuser:
    #             if user.is_staff:
    #                 return Response('Cannot delete a superuser')
    #         else:
    #             user.delete()
    #             return Response('User with id f{pk} is deleted')
    return Response(serializer.data)


def hello(request):
    return HttpResponse('Start implement auth')
