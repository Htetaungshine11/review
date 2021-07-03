"""
ASGI config for review project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'review.settings')
a= get_asgi_application()
from channelsrev.urls import urlpatterns
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter,ProtocolTypeRouter
application = ProtocolTypeRouter({
    "http":a,
    "websocket":AuthMiddlewareStack(URLRouter(urlpatterns))
})
