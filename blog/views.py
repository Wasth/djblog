from django.shortcuts import render
from django.views.generic import ListView, FormView

from blog.forms import SignInForm
from blog.models import Post


class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class SignIn(FormView):
    template_name = 'blog/signin.html'
    form_class = SignInForm
    success_url = '/'

    # def from_valid(self, form):
