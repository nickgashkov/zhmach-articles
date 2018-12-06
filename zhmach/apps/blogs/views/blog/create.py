from django.apps import apps
from django.views import generic

from zhmach.apps.blogs.forms import BlogForm


class BlogCreateView(generic.CreateView):
    model = apps.get_model('blogs.Blog')
    template_name = 'blogs/create-update.html'

    form_class = BlogForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Добавить статью'

        return context
