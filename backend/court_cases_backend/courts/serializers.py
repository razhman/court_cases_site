from dataclasses import fields
from django.conf import settings

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['__all__']