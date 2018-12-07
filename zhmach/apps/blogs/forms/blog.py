from django import forms
from django.apps import apps


class BlogForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('blogs.Blog')
        fields = ('name', 'image', 'text')

    def __init__(self, **kwargs):
        self.user = kwargs.pop('user')

        super().__init__(**kwargs)

        self.tune_fields()

    def tune_fields(self):
        self.tune_name_field()
        self.tune_text_field()

    def tune_name_field(self):
        self.fields['name'].widget.attrs.update({'class': 'input'})

    def tune_text_field(self):
        self.fields['text'].widget.attrs.update({'class': 'textarea'})

    def save(self, commit=True):
        if self.instance._state.adding:
            self.instance.author = self.user

        return super().save(commit)
