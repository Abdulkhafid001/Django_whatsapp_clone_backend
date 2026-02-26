from django.urls import re_path, path
from whatsappclone.consumers import SimpleConsumer, NotificationConsumer, ChatConsumer

websocket_urlpatterns = [
    path(r'ws/testmessage/', SimpleConsumer.as_asgi()), # type: ignore

    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()), # type: ignore
    
    re_path(r'ws/notifications/$', NotificationConsumer.as_asgi()), # type: ignore
]
