from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.auth import get_user
from chat.models import SenderModel, ReceiverModel, ChatModel, ChatKeyModel
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Setup the user1 and user2
        self.sender = await get_user(self.scope)
        reciever_id = self.scope['url_route']['kwargs']['reciever_id']
        self.reciever = await self.get_usermodel(id=reciever_id)

        if not self.sender.is_authenticated:
            await self.close()

        self.sender.sender = await self.get_sendermodel(user=self.sender)
        self.reciever.receiver = await self.get_receivermodel(user=self.reciever)

        # Get the key from ChatKeyModel and create room name
        usernames = [self.sender.username]
        if self.sender.id != self.reciever.id:
            usernames.append(self.reciever.username)
        
        chatkey = await database_sync_to_async(ChatKeyModel.get_by_usernames)(usernames)
        self.room_name = f'chat_room_{chatkey.key}'
        
        # Add the room name to channel layer
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        # Accept the request
        await self.accept()
    
    async def disconnect(self, close_code):
        # Remove the room name to channel layer
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
        # Decode the message
        text_data_as_json = json.loads(text_data)
        message = text_data_as_json['message']

        # Setup message for ChatModel
        message = {
            'sender': self.sender.sender,
            'receiver': self.reciever.receiver,
            'text': message
        }

        # Save the message to database
        await self.create_chatmodel(**message)

        # Get the created ChatModel, format the chat timestamp,
        # then send it to the channel layer
        chatmodel = await self.get_latest_chatmodel(**message)
        timestamp = f'{chatmodel.timestamp.date()} - {str(chatmodel.timestamp.time())[:8]}'
        chatmodel = {
            'sender_username': self.sender.username,
            'receiver_username': self.reciever.username,
            'text': chatmodel.text,
            'timestamp': timestamp
        }
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'send.message',
                'chatmodel': chatmodel
            }
        )
    
    async def send_message(self, event):
        # Get the chatmodel from event then make it as json format
        message = json.dumps({'chatmodel': event['chatmodel']})

        # Send the message to websocket
        await self.send(
            text_data=message
        )

    @database_sync_to_async
    def get_usermodel(self, **kwargs):
        return User.objects.get(**kwargs)
    
    @database_sync_to_async
    def get_receivermodel(self, **kwargs):
        return ReceiverModel.objects.get(**kwargs)
    
    @database_sync_to_async
    def get_sendermodel(self, **kwargs):
        return SenderModel.objects.get(**kwargs)
    
    @database_sync_to_async
    def get_latest_chatmodel(self, **kwargs):
        return ChatModel.objects.filter(**kwargs).last()
    
    @database_sync_to_async
    def create_chatmodel(self, **kwargs):
        return ChatModel.objects.create(**kwargs)