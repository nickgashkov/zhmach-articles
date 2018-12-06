from django.apps import apps
from django.views import generic


class BlogListView(generic.ListView):
    model = apps.get_model('blogs.Blog')
    template_name = 'blogs/list.html'
