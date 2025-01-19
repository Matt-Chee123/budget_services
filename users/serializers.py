from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username,password=password)

        if not user:
            raise AuthenticationFailed('Invalid Credentials')

        attrs['user'] = user
        attrs['token'] = 'test'
        return attrs

