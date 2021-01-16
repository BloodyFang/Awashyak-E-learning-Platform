from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ForumListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'forum.html'


class ForumDetailView(DetailView):
    model = Post
    template_name = 'forum_detail.html'



