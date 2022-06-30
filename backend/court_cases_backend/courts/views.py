from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourtCasesSerializer, CustomUserSerializer
from .models import CustomUser, CourtCases

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CourtCasesViewSet(viewsets.ModelViewSet):
    queryset = CourtCases.objects.all()
    serializer_class  = CourtCasesSerializer