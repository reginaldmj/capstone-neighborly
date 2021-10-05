from django import forms
from .models import NeighborlyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(forms.ModelForm):
    class Meta:
        model = NeighborlyUser
        fields = ['username', 'password', 'email','display_name', 'age']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class NeighborlyUserCreationForm(UserCreationForm):

    class Meta:
        model = NeighborlyUser
        fields = ('username', 'display_name', 'email')

class NeighborlyUserChangeForm(UserChangeForm):
    class Meta:
        model = NeighborlyUser
        fields = ('username', 'email')

