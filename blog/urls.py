from django.urls import path

from blog.views import EditPost, PostList, SignIn, PostDetail, log_out, SignUp, MyPostList, CreatePost
from blog.views import add_tag, del_tag, set_category, del_category

urlpatterns = [
    path('', PostList.as_view(), name='index'),

    path('myposts/', MyPostList.as_view(), name='myposts'),
    path('newpost/', CreatePost.as_view(), name='newpost'),
    path('post/<pk>/', PostDetail.as_view(), name='detail'),
    path('edit/post/<pk>/', EditPost.as_view(), name='edit'),

    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', log_out, name='logout'),

    path('at/<tag>', add_tag, name='add_tag'),
    path('dt/<tag>', del_tag, name='del_tag'),

    path('ac/<category>', set_category, name='set_cat'),
    path('dc/<category>', del_category, name='del_cat'),
]
