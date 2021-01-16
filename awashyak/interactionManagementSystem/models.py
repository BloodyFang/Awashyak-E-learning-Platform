from django.db import models
from django.contrib.auth.models import User
from courseManagementSystem.models import Module
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='forum_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title