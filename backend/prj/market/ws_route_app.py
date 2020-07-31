from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from market.consumer import MarketConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
            URLRouter([
                re_path(r'market$', MarketConsumer),
            ])
    )
})

