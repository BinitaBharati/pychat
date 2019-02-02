from django.conf.urls import url

from . import consumers

#WebSocket routes - Ref: https://channels.readthedocs.io/en/stable/tutorial/part_1.html

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]