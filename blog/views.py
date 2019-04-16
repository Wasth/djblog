from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
