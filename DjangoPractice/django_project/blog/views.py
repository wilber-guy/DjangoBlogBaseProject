from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import User



def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context )

class PostListView(ListView):
    model = Post
    # naming convention for : app/model_viewtype.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # sets how many posts to show per pagination
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    # naming convention for : app/model_viewtype.html
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # sets how many posts to show per pagination
    paginate_by = 5

    def get_queryset(self):
        # get an object from database if exists or returns 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # we are filtering only the user is aiuthor
        return Post.objects.filter(author=user).order_by('-date_posted')




class PostDetailView(DetailView):
    model = Post

# first inherit from LoginRequiredMixin, then inherit from createView
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # naming convention for create: app/model_form.html
    #template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        # for this instance of the form, change the author to this requests user
        form.instance.author = self.request.user
        # runs the parent class with our change of author of form instance
        return super().form_valid(form)

# class used for updating posts
# requires user to be the original author of the post that is being updated
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        # gets current post object we are trying to update
        post = self.get_object()
        # checks if current request user is the post author
        if self.request.user == post.author:
            return True
        else:
            return False
    
    def form_valid(self, form):
        # for this instance of the form, change the author to this requests user
        form.instance.author = self.request.user
        # runs the parent class with our change of author of form instance
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # on succesful delete send user to 
    success_url = '/'

    def test_func(self):
        # gets current post object we are trying to update
        post = self.get_object()
        # checks if current request user is the post author
        if self.request.user == post.author:
            return True
        else:
            return False

    

    


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


