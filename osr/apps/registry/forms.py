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
<<<<<<< HEAD
        fields = ('__all__')

class UMOForm(forms.ModelForm):
    class Meta:
        model = models.UMO
        fields = ('__all__')

class PrimaryForm(forms.ModelForm):
    class Meta:
        model = models.Primary
        fields = ('__all__')
=======
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
>>>>>>> 477aaca558b6b5350d46ae44d7a384fca1c7d27c
