from rest_framework import serializers
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.six import text_type
from .models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'group_id')
            

class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for creating user objects."""
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'group_id', 'tokens')
        extra_kwargs = {'password': {'write_only': True}}

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = text_type(tokens)
        access = text_type(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.group_id = validated_data['group_id']
        user.set_password(validated_data['password'])
        user.save()    
        return user

