from django.apps import apps
from django.views import generic


class BlogDetailView(generic.DetailView):
    model = apps.get_model('blogs.Blog')
    template_name = 'blogs/detail.html'
