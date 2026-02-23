"""
ASGI config for whatsappclone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import whatsappclone.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatsappclone.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    # HTTP requests handled normally by Django
    'http': get_asgi_application(),
    # WebSocket requests handled by Channels
    'websocket': AuthMiddlewareStack(
        URLRouter(whatsappclone.routing.websocket_urlpatterns)
    )
})
