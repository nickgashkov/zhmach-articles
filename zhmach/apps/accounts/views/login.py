from django.contrib.auth.views import LoginView as DjangoLoginView

from zhmach.apps.accounts.forms import AuthenticationForm


class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'

    form_class = AuthenticationForm
