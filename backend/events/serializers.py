from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("event_name", "event_date", "event_time", "event_location", "event_image", "is_liked", "user",)


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirmPassword = serializers.CharField(write_only=True)

    def validate(self, data):
        password1 = data.get('password')
        password2 = data.get('confirmPassword')

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match")
        
        if User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError("Username already taken")

        if User.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError("Email already taken")

        return data

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid username or password")
        else:
            raise serializers.ValidationError("Both username and password are required")
        
        data['user'] = user
        return data