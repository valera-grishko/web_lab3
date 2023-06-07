from rest_framework import serializers
from django.contrib.auth import get_user_model

from .tasks import send_registration_message

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'birth_date', 'gender', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_registration_message.delay(user.email)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
