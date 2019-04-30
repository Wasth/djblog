from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView
from django.contrib import messages

from blog.forms import SignInForm
from blog.models import Post, Category, Tag, Profile


class SidebarContext:
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(SidebarContext, self).get_context_data(**kwargs)
        context['ctx'] = {
            'categories': Category.objects.all(),
            'tags': Tag.objects.all(),
            'popular_blogers': Profile.objects.all()
        }
        return context


class PostList(ListView, SidebarContext):
    model = Post
    paginate_by = 5
    ordering = ['-pub_date']
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category = self.request.GET.get('c')
        sorting = self.request.GET.get('s')
        print('Category - ' + str(category))
        print('Sorting - ' + str(sorting))
        return Post.objects.all()


class PostDetail(DetailView, SidebarContext):
    model = Post
    template_name = 'blog/detail.html'


class SignIn(FormView):
    template_name = 'blog/signin.html'
    form_class = SignInForm
    success_url = '/'

    # def from_valid(self, form):


def log_out(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Successful log out')

    return redirect('index')
