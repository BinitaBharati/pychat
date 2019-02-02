from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import mainmodule.routing

#WebSocket routes - Ref: https://channels.readthedocs.io/en/stable/tutorial/part_1.html

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            mainmodule.routing.websocket_urlpatterns
        )
    ),
})