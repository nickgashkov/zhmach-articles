from django.contrib.auth.forms import (
    AuthenticationForm as DjangoAuthenticationForm,
)


class AuthenticationForm(DjangoAuthenticationForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tune_fields()

    def tune_fields(self):
        self.tune_username_field()
        self.tune_password_field()

    def tune_username_field(self):
        self.fields['username'].widget.attrs.update({'class': 'input'})

    def tune_password_field(self):
        self.fields['password'].widget.attrs.update({'class': 'input'})
