from django.conf.urls import url
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
import django_eventstream

urlpatterns = [
    url(r'^events/', AuthMiddlewareStack(
        URLRouter(django_eventstream.routing.urlpatterns)
    ), {'channels': ['test']}),
    url(r'', AsgiHandler),
]
application = ProtocolTypeRouter({
    'http': URLRouter(urlpatterns),
})