from django import forms

class AddPostForm(forms.Form):
    body = forms.CharField()