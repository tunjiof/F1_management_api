from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import permissions

# Create your views here.

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created sucessfully"}, status=status.HTTP_201_CREATED)

        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        
        if user is not None:
            access = AccessToken.for_user(user)
            print({
                "access": access,
                "access_type": type(access)
            },   "access_token")
            return Response({"token": str(access)}, status=status.HTTP_200_OK)
        else:
             return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)