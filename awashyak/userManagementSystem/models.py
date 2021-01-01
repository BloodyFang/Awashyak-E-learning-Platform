from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

#UserProfileInfo has 1 to 1 relationship with user profile so that user can have their type and profile pic linked with User table.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)

    #additional
    userType = models.CharField(max_length=150,null=False)
    profilePic = models.ImageField(upload_to  = 'profile_pics/', blank= True, default ='profile.png')

    def __str__(self):
        return self.user.username