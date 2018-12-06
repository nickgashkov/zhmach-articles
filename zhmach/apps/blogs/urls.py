from django.contrib.auth.decorators import login_required
from django.urls import path

from zhmach.apps.blogs.views.blog import (
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView,
)

app_name = 'blogs'

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/add/', login_required(BlogCreateView.as_view()), name='blog-create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/<int:pk>/update/', login_required(BlogUpdateView.as_view()), name='blog-update'),
    path('blogs/<int:pk>/delete/', login_required(BlogDeleteView.as_view()), name='blog-delete'),
]
