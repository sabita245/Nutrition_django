from django.urls import path
from .views import *

urlpatterns = [
    path('customerprofile/',CustomerCreate.as_view(),name='customerprofile'),
    
]