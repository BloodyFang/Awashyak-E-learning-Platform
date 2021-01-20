from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ForumListView,ForumCreateView,ForumUpdateView,ForumDeleteView

urlpatterns = [
   path('forum/<int:pk>/',ForumListView.as_view(),name='forum'),
   path('post/<int:pk>/',views.post_detail, name='post_detail'),
   path('post/new/<int:pk>',ForumCreateView.as_view(),name='post_new'),
   path('post/,<int:pk>/edit/',ForumUpdateView.as_view(),name='post_edit'),
   path('post/<int:pk>/delete/',ForumDeleteView.as_view(),name='post_delete'),
  



  
]