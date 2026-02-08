from rest_framework import serializers
from django.db.models import fields
from rest_framework.decorators import api_view
from .models import WcUser, AccessToken


class AccessTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessToken
        fields = ('token')


class WcUserSerializer(serializers.ModelSerializer):
    token = AccessTokenSerializer(read_only=True)

    class Meta:
        model = WcUser
        fields = ('username', 'password', 'is_active', 'is_superuser', 'is_staff', 'token')
