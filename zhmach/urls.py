from django.urls import path, include

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('blogs/', include('zhmach.apps.blogs.urls', namespace='blogs')),
]
