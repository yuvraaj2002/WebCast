from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer, RegisterSerializer,GoogleLoginSerializer
from django.contrib.auth.backends import ModelBackend
from django.utils.timezone import now
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.views import TokenRefreshView


# Views
class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):    
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=201)
        return Response(serializer.errors, status=400)

class SigninView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not email:
            return Response({'error': 'Username and email are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(email=email)
        username = user.username
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user:
            authenticated_user.last_login = now()
            authenticated_user.save(update_fields=['last_login'])  
            
            return Response(UserSerializer(authenticated_user).data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class RefreshTokenView(TokenRefreshView):
    permission_classes = [AllowAny]


class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = GoogleLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create_or_login()
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)
    
class UserProfileEditView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)