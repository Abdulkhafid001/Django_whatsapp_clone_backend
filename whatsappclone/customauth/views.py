from rest_framework import status
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WcUser, RefreshToken as WcRefreshToken
from .serializers import WcUserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'get_all_users': 'users/',
        'Search by Username': '/?username=username',
        'Create': '/create',
        'Update': 'update/pk',
        'Delete': '/item/pk/delete',
        'Login':  '/login',
        'ObtainJWTToken': '/obtaintoken',
        'RefreshJWTToken': '/refreshtoken',
    }
    return Response(api_urls)


@api_view(['POST'])
def create_user(request):
    """ Creates a new user with username and password and associates user to an access token.  {"username": "", "password": ""} """
    serializer = WcUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # create access token for user
        create_user_access_token(request.data['username'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def create_user_access_token(username):
    "this function automatically creates an access token user once created"
    user_model = get_user_model()
    try:
        user = user_model.objects.get(username=username)
        print("block executed")
        # generate refresh token
        user_refresh_token = RefreshToken.for_user(user)
        # create refresh token record in DB
        WcRefreshToken.objects.create(user=user, token=user_refresh_token)
    except WcUser.DoesNotExist:
        return 'cannot create user as user does not exist'


@api_view(['POST'])
def login(request):
    username = request.data["username"]
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    print('found: ', user)
    if user is not None:
        print('block executed')
        login(request, user)
        return JsonResponse({'message: ': 'Details correct... User is logged in'}, status=status.HTTP_200_OK)
    return JsonResponse({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_users(request):
    users = WcUser.objects.all()
    serializer = WcUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_by_id(request, id):
    try:
        wc_user = WcUser.objects.get(id=id)
        if wc_user.__class__.objects.exists():
            serializer = WcUserSerializer(wc_user)
            return Response(serializer.data)
    except WcUser.DoesNotExist:
        return Response('User with Id does not exist')


@api_view(['GET'])
def get_user_by_username(request, username):
    try:
        wc_user = WcUser.objects.get(username=username)
        if wc_user.__class__.objects.exists():
            serializer = WcUserSerializer(wc_user)
            return Response(serializer.data)
    except WcUser.DoesNotExist:
        return Response('User with username does not exist')


@api_view(['GET'])
def delete_user(request, id):
    try:
        user = WcUser.objects.get(id=id)
        if request.user.is_authenticated:
            if request.user.is_superuser:
                # check if current logged in user
                if user.username == request.user.username:
                    return Response('cannot delete yourself 🤣🤣')
                else:
                    user.delete()
                    return Response(f'{user.username} deleted', status=status.HTTP_204_NO_CONTENT)
    except WcUser.DoesNotExist:
        return Response(f'User with id {id} does not exist in system')


def hello(request):
    return HttpResponse('Start implement auth')
