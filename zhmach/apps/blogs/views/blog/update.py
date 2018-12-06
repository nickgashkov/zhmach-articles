from django.apps import apps
from django.views import generic

from zhmach.apps.blogs.forms import BlogForm


class BlogUpdateView(generic.UpdateView):
    model = apps.get_model('blogs.Blog')
    template_name = 'blogs/create-update.html'

    form_class = BlogForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs
