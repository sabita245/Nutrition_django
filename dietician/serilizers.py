from rest_framework.serializers import ModelSerializer
from .models import *


class AboutSerializer(ModelSerializer):
    class Meta:
        model= About
        fields= "__all__"
    
class FeeSerializer(ModelSerializer):
    class Meta:
        model= Fee
        fields="__all__"
class ContactSerializer(ModelSerializer):
    class Meta:
        model= Contact
        fields="__all__"
class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"    