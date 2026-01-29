from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from chat.models import Post


def welcome_view(request):
    return HttpResponse("App running")


def get_all_blog_posts(request):
    all_posts = Post.objects.all()
    return HttpResponse(all_posts)
