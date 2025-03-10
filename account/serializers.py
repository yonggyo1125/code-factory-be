from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
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

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'