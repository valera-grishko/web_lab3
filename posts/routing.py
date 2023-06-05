from django.urls import re_path

from .consumers import MessageConsumer, CommentConsumer

websocket_urlpatterns = [
    re_path('ws/messages/', MessageConsumer.as_asgi()),
    re_path('ws/comments/', CommentConsumer.as_asgi()),
]
