from rest_framework import status
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WcUser, WcRefreshToken
from .serializers import WcUserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import authenticate, login, logout


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'get_all_users': 'users/',
        'Search by Username': '/?username=username',
        'Create': '/create',
        'Update': 'update/pk',
        'Delete': '/item/pk/delete',
        'Login':  '/login',
        'Logout':  '/logout',
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
        username = request.data['username']
        # create_user_refresh_token(username)
        return Response({'data': serializer.data, 'token': str(create_user_refresh_token(username))}, status=status.HTTP_201_CREATED)
    return Response({"errors": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def create_user_refresh_token(username):
    "this function automatically creates a refresh token user once created and then returns the tokens"
    user_model = get_user_model()
    try:
        user = user_model.objects.get(username=username)
        # generate refresh token
        user_refresh_token = RefreshToken.for_user(user)
        # save refresh token record to DB
        WcRefreshToken.objects.create(user=user, token=user_refresh_token)
        # user_tokens = {'refreshtoken': user_refresh_token,
        #                'accesstoken': user_refresh_token.access_token}
        return user_refresh_token.access_token
    except WcUser.DoesNotExist:
        return 'cannot create user as user does not exist'


@api_view(['POST'])
def login_user(request):
    username = request.data["username"]
    password = request.data['password']
    login_success = False
    user = authenticate(request, username=username, password=password)
    print('found: ', user)
    if user is not None:
        print('block executed')
        # check if refresh token is still valid, if valid send access token to frontend, else, send info to redirect to login
        login(request, user)
        # get refresh token and use to send access token to frontend and continue from there.
        login_success = True
        # get user to save in local storage for logout impl.
        user_model = get_user_model()
        user_info = user_model.objects.get(username=username).username
        print('username from usermodel:', user_info)
        data = {'username': user_info, 'loginSuccessful': login_success,
                'accesstoken': str(create_user_refresh_token(username))}
        return Response(data=data, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_user(request):
    username = request.data['username']
    logout_successful = False
    user_model = get_user_model()
    user = user_model.objects.get(username=username)
    if user.is_authenticated:
        logout(request)
        logout_successful = True
    return Response({'data': username, 'logoutSuccessful': logout_successful}, status=status.HTTP_200_OK)


def get_user_refresh_token(username):
    user_model = get_user_model()
    try:
        user = user_model.objects.get(username=username)
        refresh_token = WcRefreshToken.objects.get(user=user)
        return (refresh_token.token)
    except WcUser.DoesNotExist:
        return "no user found"


def send_user_access_token(request):
    pass


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
