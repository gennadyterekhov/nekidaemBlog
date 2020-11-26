from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog import views
from blog.models import Post



urlpatterns = [
    path('', views.index, name='index'),
    path('u/', views.UserListView.as_view(template_name="user_list.html"), name='user_list'),
    # path('u/<int:user_id>/', views.UserDetailView.as_view(template_name="user_detail.html"), name='user_detail'),
    path('p/', views.PostListView.as_view(template_name="post_list.html"), name='post_list'),
    path('login/', TemplateView.as_view(template_name="login.html"), name='login'),
    path('loginCheck/', views.loginCheck, name='login'),
]