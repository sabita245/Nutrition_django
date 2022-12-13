from django.urls import path
from .views import *

urlpatterns = [
    path('profile/',CustomerCreate.as_view(),name='customerprofile'),
    
]