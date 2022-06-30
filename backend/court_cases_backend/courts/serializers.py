from dataclasses import fields
from django.conf import settings

from rest_framework import serializers
from .models import CustomUser, CourtCases

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'surename', 'patronymic']

class CourtCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtCases
        fields = '__all__'