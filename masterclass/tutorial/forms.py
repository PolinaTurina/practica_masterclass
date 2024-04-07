from django import forms

from . models import *


class BronForm(forms.ModelForm):
    class Meta:
        model = Bron
        fields = ['count']
        exclude = ['user_id', 'masterclass_id']
        widgets = {
            'user_id': forms.HiddenInput(),
            'masterclass_id': forms.HiddenInput(),
        }