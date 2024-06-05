from django.contrib.auth.models import User
from django.forms import TextInput
from django import forms


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

