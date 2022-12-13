from django.shortcuts import render
from rest_framework.generics import *
from .models import About
from .serilizers import *

# Create your views here.
class AboutUs(ListCreateAPIView):
    serializer_class=AboutSerializer
    queryset=About.objects.all()
class ContactUs(ListCreateAPIView):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()

class FeePlan(ListCreateAPIView):
    serializer_class=FeeSerializer
    queryset=Fee.objects.all()
class FAQ(ListCreateAPIView):
    serializer_class=FAQSerializer
    queryset=FAQ.objects.all()


