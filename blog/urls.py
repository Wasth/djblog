from django.urls import path

from blog.views import PostList, SignIn, PostDetail, log_out, SignUp

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('post/<pk>/', PostDetail.as_view(), name='detail'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', log_out, name='logout'),
]
