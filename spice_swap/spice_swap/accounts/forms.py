from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Your passwords don't match.",
        'password_too_short': "Your password must contain at least 8 characters.",
        'password_common': "Your password is too common.",
        'password_entirely_numeric': "Your password can't be entirely numeric.",
    }

