from rest_framework import serializers
from chat.models import Message

class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'room', 'content', 'timestamp']