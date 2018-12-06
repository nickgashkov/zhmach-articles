from django import forms
from django.apps import apps


class BlogForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('blogs.Blog')
        fields = ('name', 'text')

    def __init__(self, **kwargs):
        self.user = kwargs.pop('user')

        super().__init__(**kwargs)

    def save(self, commit=True):
        if self.instance._state.adding:
            self.instance.author = self.user

        return super().save(commit)
