from django.apps import apps
from django.urls import reverse_lazy
from django.views import generic


class BlogDeleteView(generic.DeleteView):
    model = apps.get_model('blogs.Blog')

    success_url = reverse_lazy('blogs:blog-list')
