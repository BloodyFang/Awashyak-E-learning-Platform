from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE,primary_key=True)

    #additional
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    userType = models.CharField(max_length=150,null=False)
    profilePic = models.ImageField(upload_to  = 'profile_pics', blank= True)

    def __str__(self):
        return self.user.username