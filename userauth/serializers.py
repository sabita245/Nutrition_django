from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','age','password']












# from django.db import models
# from django.db.models import fields
# from rest_framework.serializers import ModelSerializer
# from .models import *

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"