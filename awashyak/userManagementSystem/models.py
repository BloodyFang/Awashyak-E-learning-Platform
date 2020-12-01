from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)

    #additional
   
    userType = models.CharField(max_length=150,null=False)
    profilePic = models.ImageField(upload_to  = 'profile_pics/', blank= True, default ='profile.png')

    def __str__(self):
        return self.user.username