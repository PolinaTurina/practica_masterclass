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

class FilterForm(forms.Form):
    CHOICES = (
        ('1', 'Min'),
        ('2', 'Max'),
        ('3', 'Сброс'),
    )
    filter = forms.ChoiceField(choices=CHOICES)