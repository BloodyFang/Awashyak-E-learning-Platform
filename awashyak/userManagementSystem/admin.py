from django.contrib import admin
from .models import UserProfileInfo
# Register your models here.

@admin.register(UserProfileInfo)
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','userType','profilePic')
    