from django.contrib import admin
from .models import UserProfileInfo
# Register your models here.

# Adding UserProfileInfo to Django Admin panel.
@admin.register(UserProfileInfo)
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','userType','profilePic') 
    