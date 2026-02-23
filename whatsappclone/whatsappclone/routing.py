from django.urls import re_path, path
from whatsappclone.consumers import SimpleConsumer

websocket_urlpatterns = [
    path(r'ws/chat/', SimpleConsumer.as_asgi()),
]
