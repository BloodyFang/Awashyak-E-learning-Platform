from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('register/', userRegistration , name='register'),
    path('register/save/',userRegistrationSave),
    path('login/', userLogin , name='login'),
    path('login/success/', loginAuth),
    path('logout/',logoutView, name='logout'),
    path('profile/',profilePage, name='profile'),
    path('delete/',deleteProfile, name = 'delete'),
    path('update/',updateProfilePage, name='update'),
    path('update/save/',updateProfile),
    path('update/updatePassword/', changePassword,name='updatePassword'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('student_dashboard/', studentDashboard, name = 'studentDashboard'),
    path('teacher_dashboard/', teacherDashboard, name = 'teacherDashboard'),
    
    
]