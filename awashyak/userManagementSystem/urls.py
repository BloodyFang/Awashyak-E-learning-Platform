from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   
    path('register/', userRegistration , name='register'),
    path('register/save/',userRegistrationSave),
    path('login/', userLogin , name='login'),
    path('login/success/', loginAuth),
    path('logout/',logoutView, name='logout'),
    path('profile/<int:id>',profilePage, name='profile'),
    path('update/<int:id>',updateProfilePage, name='update'),
    path('update/save/<int:id>',updateProfile),
    
    
]