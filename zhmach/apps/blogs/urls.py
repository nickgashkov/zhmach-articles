from django.urls import path

from zhmach.apps.blogs.views.blog import (
    BlogCreateView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView,
)

app_name = 'blogs'

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/add/', BlogCreateView.as_view(), name='blog-create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
]
