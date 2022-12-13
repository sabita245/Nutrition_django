from django.urls import path
from .views import *

urlpatterns = [
    path('profile/',AboutUs.as_view(),name='profile'),
    path('contact/',ContactUs.as_view(),name='contact'),
    path('fee/',FeePlan.as_view(),name='fee'),
    path('faq/',FAQ.as_view(),name='faq'),
    
]