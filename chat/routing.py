from django.urls import path
from chat import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:reciever_id>/', consumers.ChatConsumer.as_asgi())
]