from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView
from django.contrib import messages

from blog.forms import SignInForm, SignUpForm
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


class SignUp(FormView):
    template_name = 'blog/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
        user.save()
        messages.add_message(self.request, messages.INFO, 'Successful sign up!')
        return super().form_valid(form)


def log_out(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Successful log out')

    return redirect('index')
