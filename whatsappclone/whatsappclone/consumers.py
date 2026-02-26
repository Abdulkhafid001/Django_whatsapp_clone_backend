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


class NotificationConsumer(AsyncWebsocketConsumer):
    pass
