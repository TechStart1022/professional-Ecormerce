from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from userauths.serializer import RegisterSerializer,MyTokenObtainPairSerializer,UserSerializer,ProfileSerializer
from rest_framework import generics
from userauths.models import *
from rest_framework.permissions import IsAuthenticated,AllowAny




class TokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
# Create your views here.
