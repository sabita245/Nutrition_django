from rest_framework.serializers import ModelSerializer
from .models import *

class CustomerSerializer(ModelSerializer):
    class Meta:
        model=CostumerProfile
        fields= ["customer_name","customer_age","customer_height","food","gender"]