from django.db import models
from django.contrib.auth.models import User
from courseManagementSystem.models import Module
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import pre_save
from interactionManagementSystem.utils import unique_slug_generator
from django.contrib.auth import get_user_model
from courseManagementSystem.models import Course
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    course = models.ForeignKey(Course,related_name='forum_course',on_delete=models.CASCADE)
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

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])

    # def get_absolute_url_2(self):
    #     return reverse('post_new',args=[str(self.course.id)])

def slug_save(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance,instance.title,instance.slug)

pre_save.connect(slug_save,sender = Post)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='comment_user')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post}'

        