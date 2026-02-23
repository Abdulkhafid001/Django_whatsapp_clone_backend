import json
from channels.generic.websocket import WebsocketConsumer


class SimpleConsumer(WebsocketConsumer):

    def connect(self):
        """Called when WebSocket connection is opened"""
        # Accept the connection
        self.accept()

        # Send welcome message
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            # 'message': 'You are now connected Yslcodes',
            'message': wc_users
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
