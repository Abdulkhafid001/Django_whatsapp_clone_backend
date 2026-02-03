from rest_framework import serializers
from django.db.models import fields
from rest_framework.decorators import api_view
from .models import WcUser


class WcUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WcUser
        fields = ('username', 'password', 'is_active', 'is_superuser')
