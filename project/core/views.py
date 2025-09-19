from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

def test_view(request):
    return HttpResponse("Working right")
