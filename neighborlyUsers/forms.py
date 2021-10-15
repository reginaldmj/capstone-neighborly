from django import forms
from .models import NeighborlyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    email = forms.EmailField(max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class NeighborlyUserCreationForm(UserCreationForm):
    class Meta:
        model = NeighborlyUser
        fields = ('username', 'display_name', 'email')


class NeighborlyUserChangeForm(forms.ModelForm):
    class Meta:
        model = NeighborlyUser
        fields = ['display_name', 'email', 'age', ]
