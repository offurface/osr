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
        fields = [
            'name',
            'surname',
            'patronymic',
            'date_of_birth',
            'gender',
            'location',
            'telephone',
            'sports_facility',
            'swimming_skills',
            'school_progress',
            'sport_desire',
            'coach',
            'parent',
            'sport_type',
            'rank',
        ]
