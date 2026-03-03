from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from chat.models import PostNotification


def welcome_view(request):
    return HttpResponse("App running")


class PostNotificationDetailView(DetailView):
    model = PostNotification
    template_name = 'postnotification.html'
    context_object_name = 'postnotification'