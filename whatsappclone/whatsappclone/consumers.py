import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer, JsonWebsocketConsumer
from customauth.services import get_all_users


class SimpleConsumer(JsonWebsocketConsumer):

    def connect(self):
        """Called when WebSocket connection is opened"""
        # Accept the connection
        self.accept()

        # Send welcome message
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            # 'message': 'You are now connected Yslcodes',
            'message': get_all_users()
        }))

    def disconnect(self, close_code):
        """Called when WebSocket connection is closed"""
        pass

    def receive(self, text_data):
        """Called when message is received from client"""
        data = json.loads(text_data)
        message = data['message']
        print('sent from user : ', message)

        # Echo message back to client
        self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message
        }))


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Called when a Websocket is opened."""

        # creating a room
        self.room_name = self.scope['url_route']['kwargs']['room_name']# type: ignore
        self.room_group_name = f'chat_{self.room_name}'

        # Join a room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self):
        """Called when a websocket is disconnected."""

        # leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """Called when a websocket message is received."""

        data = json.loads(text_data)
        message = data['message']
        username = data.get('username', 'AnonymousUser')

        # send message to all users in the channel group
        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'message': message,
            'username': username
        })

    async def chat_message(self, event):
        """Handles messages sent to the group"""
        await self.send(text_data=json.dumps(
            {
                'type': 'chat_message',
                'message': event['message'],
                'username': event['username']
            }
        ))

    def close(self):
        pass


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Called when a websocket connection is opened"""
        await self.accept()

        await self.send(text_data=json.dumps({'message': 'Notification Websocket connected successfully'}))

    async def receive(self, data):
        """Called when a message is received from the client"""
        data = await json.loads(data)
        message = data['message']
        print(message)

        await self.send(text_data=json.dumps({'message': 'notification message received'}))

    async def disconnect(self):
        pass
