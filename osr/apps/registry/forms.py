from django import forms
from . import models

class SportTypeForm(forms.ModelForm):
    class Meta:
        model = models.Sport_type
        fields = ('__all__')

class CoachForm(forms.ModelForm):
    class Meta:
        model = models.Coach
        fields = ('__all__')

class ParentForm(forms.ModelForm):
    class Meta:
        model = models.Parent
        fields = ('__all__')

class SportsmanForm(forms.ModelForm):
    class Meta:
        model = models.Sportsman
        fields = ('__all__')

class UMOForm(forms.ModelForm):
    class Meta:
        model = models.UMO
        fields = ('__all__')

class PrimaryForm(forms.ModelForm):
    class Meta:
        model = models.Primary
        fields = ('__all__')
