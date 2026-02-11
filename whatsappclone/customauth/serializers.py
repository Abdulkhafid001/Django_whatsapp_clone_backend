from rest_framework import serializers
from django.db.models import fields
from rest_framework.decorators import api_view
from .models import WcUser, RefreshToken


class RefreshTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefreshToken
        fields = ('token')


class WcUserSerializer(serializers.ModelSerializer):
    token = RefreshTokenSerializer(read_only=True)

    class Meta:
        model = WcUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = WcUser.objects.create(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
