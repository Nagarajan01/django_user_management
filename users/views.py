from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework import generics


from .utils import get_tokens_for_user
from .serializers import RegistrationSerializer, PasswordChangeSerializer, UserSerializer, PostSerializer
from .models import MyUser, Item

class RegistrationView(APIView):
    def post(self, request):
        a = request.data
        serializer = RegistrationSerializer(data=a)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
class LoginView(APIView):
    def post(self, request):
        a = request.data
        if 'email' not in a or 'password' not in a:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = a['email']
        password = a['password']
        user = authenticate(request, email=email, password=password)
        print(request.data)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

      
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


      
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request):
        serializer = PasswordChangeSerializer(context={'request': request}, data=request.data.dict())  #pass posted data as parameters to PasswordChangeSerializer functions
        serializer.is_valid(raise_exception=True)     # check serializer is valid or not
        request.user.set_password(serializer.validated_data['new_password'])  # if valid means new password will update password 
        request.user.save()  
        return Response({'msg': 'Password Successfully Updated'}, status=status.HTTP_200_OK) 
        

class UserList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class Product_List(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = PostSerializer