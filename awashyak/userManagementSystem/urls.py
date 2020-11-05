from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   
    path('register/', userRegistration , name='register'),
   
    
    
]