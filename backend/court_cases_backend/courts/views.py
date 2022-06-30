from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CourtCasesSerializer, CustomUserSerializer
from .models import CustomUser, CourtCases

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_users(request):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer(queryset, many=True)

    return Response(serializer_class.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_courts(request):
    user = request.user
    
    if user.is_admin:
        queryset = CourtCases.objects.all()
    else:
        queryset = CourtCases.objects.filter(user_id=user.id)

    serializer_class = CourtCasesSerializer(queryset, many=True)

    return Response(serializer_class.data)