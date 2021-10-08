from django import forms
from .models import Neighborhood
# from django.forms import ModelForm


class NeighorhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['zipcode']

# class NeighborhoodSelectForm(forms.ModelForm):
#     class Meta:
#         model = Neighborhood
