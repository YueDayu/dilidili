__author__ = 'Yue Dayu'
from django import forms
from .users import User

class ImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('image', 'cropping',)
