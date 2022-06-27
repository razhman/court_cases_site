from dataclasses import fields
from django.conf import settings

from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'surename', 'patronymic']