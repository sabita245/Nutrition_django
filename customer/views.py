from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *

# Create your views here.
class CustomerCreate(CreateAPIView):
    serializer_class=CustomerSerializer
    queryset=CostumerProfile.objects.all()
    
