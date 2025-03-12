from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class SessionTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        token['mobile'] = user.mobile
        token['gid'] = user.gid

        return token

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=6, max_length=45, allow_blank=False, trim_whitespace=True)
    password = serializers.CharField(max_length=65, allow_blank=False, trim_whitespace=True)
    email = serializers.EmailField(allow_blank=False)
    mobile = serializers.CharField(max_length=15, allow_blank=True, trim_whitespace=True)

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return instance