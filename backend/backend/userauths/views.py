from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from userauths.serializer import RegisterSerializer,MyTokenObtainPairSerializer,UserSerializer,ProfileSerializer
from rest_framework import generics
from userauths.models import *
from rest_framework.permissions import IsAuthenticated,AllowAny
import random
import shortuuid



def generate_otp():
    uuid_key = shortuuid.uuid()
    unique_key = uuid_key[:6]
    return uuid_key
class TokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
# Create your views here.
class PasswordResetEmailVerify(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_object(self):
        email = self.kwargs['email']
        user = User.objects.get(email=email)
        print("user",user)

        if user:  
            user.otp = generate_otp()
            user.save()

            uidb64 = user.pk
            otp = user.otp

            link=f"http://localhost:5173/create-new-password?otp={otp}&uidb64={uidb64}"
            print(link)
        return user 