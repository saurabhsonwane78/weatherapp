from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def signup(request):
    #added comment
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        hashed_password = make_password(request.data['password'])
        user = serializer.save(password=hashed_password)
        return Response({'user': serializer.data , 'message':'User Registration Successfull'})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("Username or password is wrong", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data , "message":'Login successful'})