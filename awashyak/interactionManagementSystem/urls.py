from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ForumListView,ForumDetailView

urlpatterns = [
   path('forum/',ForumListView.as_view(),name='forum'),
   path('post/<int:pk>/',ForumDetailView.as_view(), name='post_detail'),
  


  
]