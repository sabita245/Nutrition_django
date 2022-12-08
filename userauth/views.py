from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer

class UserRegistrationView(APIView):
    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        return Response({'msg': 'registration sucessful'})




# from django.shortcuts import render
# from rest_framework.generics import *
# from .serializers import *

# # Create your views here.
# class UserCreate(CreateAPIView):
#     serializer_class=UserSerializer
#     queryset=User.objects.all()
