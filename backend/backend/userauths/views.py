from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from userauths.serializer import RegisterSerializer,MyTokenObtainPairSerializer,UserSerializer,ProfileSerializer
from rest_framework import generics
from userauths.models import *
from rest_framework.permissions import IsAuthenticated,AllowAny
import random
import shortuuid
from rest_framework.response import Response
from rest_framework import status

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
class PasswordChangeView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request):
        payload = request.data
        otp = payload.get('otp')
        uidb64 = payload.get('uidb64')
        password = payload.get('password')

        user = User.objects.get(otp=otp,pk=uidb64)

        if(user):
            user.set_password(password)
            user.otp= ''
            user.save()
            return Response({"message":"password chaged successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"User not existed"},status=status.HTTP_404_NOT_FOUND)