from django.urls import path

from blog.views import PostList, SignIn, PostDetail, log_out

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('post/<pk>/', PostDetail.as_view(), name='detail'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('logout/', log_out, name='logout'),
]