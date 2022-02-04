from django.urls import path
from .views import (BlogListView, BlogDetailView, 
BlogCreateView,  BlogUpdateView, BlogDeleteView, TopBlogListView)
from . import views


urlpatterns = [
   path('', BlogListView.as_view(), name='home'),
   path('top_posts/', TopBlogListView.as_view(), name='top_posts'),
   path('blog/new/', BlogCreateView.as_view(), name='blog_create'),
   path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
   path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
   path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),


]