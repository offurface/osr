from django import forms
from . import models

class SportTypeForm(forms.ModelForm):
    class Meta:
        model = models.Sport_type
        fields = [
            'name',
        ]
