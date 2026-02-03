from rest_framework import status
from rest_framework import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_users': '/',
        'Search by Username': '/?username=username',
        'Create': '/create',
        'Update': 'update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)




def hello(request):
    return HttpResponse('Start implement auth')


def sign_up_brute(request):
    pass
