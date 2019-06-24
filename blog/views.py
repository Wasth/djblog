from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, FormView, DetailView
from django.contrib import messages

from blog.forms import SignInForm, SignUpForm, CreatePostForm
from blog.models import Post
from djblog.settings import SESSION_COOKIE_AGE


class PostList(ListView):
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


class MyPostList(ListView):
    model = Post
    paginate_by = 5
    ordering = ['-pub_date']
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.id).all()


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class SignIn(FormView):
    template_name = 'blog/signin.html'
    form_class = SignInForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is None:
                messages.add_message(request, messages.INFO, 'Incorrect login or password')
                return render(request, 'blog/signin.html', {
                    'form': form
                })
            else:
                if form.cleaned_data['remember_me']:
                    request.session.set_expiry(SESSION_COOKIE_AGE)
                else:
                    request.session.set_expiry(0)
                login(request, user)
                messages.add_message(request, messages.INFO, 'Successful sign in!')
                return redirect('/')


class SignUp(FormView):
    template_name = 'blog/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password'])
        user.save()
        messages.add_message(self.request, messages.INFO, 'Successful sign up!')
        return super().form_valid(form)


class CreatePost(FormView):
    template_name = 'blog/newpost.html'
    form_class = CreatePostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author_id = self.request.user.id
        post.save()
        post.tag.set(form.cleaned_data['tag'])
        post.save()
        return redirect(reverse('myposts'))


def log_out(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Successful log out')

    return redirect('index')
