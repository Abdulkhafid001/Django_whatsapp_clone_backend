from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('Start implement auth')


def sign_up_brute(request):
    pass
