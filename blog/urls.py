from django.urls import path

from blog.views import PostList, SignIn, PostDetail, log_out, SignUp, MyPostList, CreatePost
from blog.views import add_tag

urlpatterns = [
    path('', PostList.as_view(), name='index'),

    path('myposts/', MyPostList.as_view(), name='myposts'),
    path('newpost/', CreatePost.as_view(), name='newpost'),
    path('post/<pk>/', PostDetail.as_view(), name='detail'),

    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', log_out, name='logout'),

    path('at/<tag>', add_tag, name='add_tag')
]
