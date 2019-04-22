from django.urls import path

from blog.views import PostList, SignIn

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('signin/', SignIn.as_view(), name='signin')
]