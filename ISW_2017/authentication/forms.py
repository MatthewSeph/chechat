from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from authentication.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    name = forms.CharField(max_length=25, required=True, label='Nome')
    surname = forms.CharField(max_length=35, required=True, label='Cognome')
    username = forms.CharField(required=True, label='Username')
    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)

    password2 = forms.CharField(label="Conferma password", widget=forms.PasswordInput, strip=False)

    class Meta:
        model = User

        fields = ('name', 'surname', 'username', 'email', 'password1', 'password2')
        exclude = None
