from django import forms
from . import models

class SportTypeForm(forms.ModelForm):
    class Meta:
        model = models.Sport_type
        fields = [
            'name',
        ]

class CoachForm(forms.ModelForm):
    class Meta:
        model = models.Coach
        fields = [
            'name',
            'surname',
            'patronymic',
            'telephone',
            'sport_type',
        ]

class ParentForm(forms.ModelForm):
    class Meta:
        model = models.Parent
        fields = [
            'name',
            'surname',
            'patronymic',
            'status',
            'telephone',
            'email',
        ]

class SportsmanForm(forms.ModelForm):
    class Meta:
        model = models.Sportsman
        fields = ['__all__']
