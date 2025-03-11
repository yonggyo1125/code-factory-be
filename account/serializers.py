from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class SessionTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        
        profile = UserProfile.objects.filter(user=user)
        if profile: 
            token['mobile'] = profile[0].mobile
            token['gid'] = profile[0].gid
        

        return token

class UserProfileSerializer(serializers.Serializer):
    def create(self, validated_data):
        """
        회원 가입 처리 
        """
        print(f"validated_data={validated_data}")
        validated_data['user_id']=1
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        회원정보 수정 처리 
        """

        pass

    