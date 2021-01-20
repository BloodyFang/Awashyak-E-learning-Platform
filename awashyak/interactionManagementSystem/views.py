from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from courseManagementSystem.models import Course


class ForumListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'forum.html'
    login_url = 'login'

    def get(self,request,pk):
        self.object_list = self.get_queryset()
        course = get_object_or_404(Course, pk = pk)
        object_lists = Post.objects.all().filter(course_id = pk)
        paginator = Paginator(object_lists, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number) 
        return self.render_to_response({'course':course,'page_obj': page_obj,})




# class ForumDetailView(LoginRequiredMixin,DetailView):
#     model = Post
#     template_name = ' forum_detail.html'
#     login_url = 'login'

    

class ForumCreateView(LoginRequiredMixin,CreateView):
    model = Post
    # prepopulated_fields = {'slug':('title',)}
    template_name = 'post_new.html'
    fields = ['title','body',]
    login_url = 'login'

    def form_valid(self,form):
        form.instance.course = Course.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        return super(ForumCreateView,self).form_valid(form)

    



class ForumUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body',]
    login_url = 'login'

    def dispatch(self,request,*args,**kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)


class ForumDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('forum')
    login_url = 'login'

    def dispatch(self,request,*args,**kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

def post_detail(request,pk):
        post = get_object_or_404(Post, pk=pk)

        #list of active comments for this post
        comments = post.comments.filter(active=True)

        new_comment = None

        if request.method == 'POST':
            #A comment was posted
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                #create comment object but do not save to database
                new_comment = comment_form.save(commit=False)
                #Assign the current post to the comment
                new_comment.post = post
                #save the comment to the database
                new_comment.save()

        else:
            comment_form = CommentForm()
        return render(request,'forum_detail.html',{'post':post,
                        'comments':comments,'new_comment':new_comment,'comment_form':comment_form
                        })


