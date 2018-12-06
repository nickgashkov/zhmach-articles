from django.contrib.auth.views import LogoutView
from django.urls import path, include

from zhmach.apps.accounts.views.login import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('blogs/', include('zhmach.apps.blogs.urls', namespace='blogs')),
]
