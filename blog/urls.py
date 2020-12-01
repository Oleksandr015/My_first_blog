from django.urls import path
from .views import PostListView,\
    PostCreateView, \
    PostUpdateView, \
    PostDetailView,\
    PostDeleteView,\
    UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('about/', views.about, name='blog_about'),

]
