from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClienteForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'Este e-mail já existe !'})
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Newsletter(forms.Form):
    email = forms.EmailField()