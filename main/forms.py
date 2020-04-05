from django import  forms
from .models import  Country,NewCases

class Country_form(forms.ModelForm):
    class Meta:
        model=Country
        fields=[
        'country_name',
        'total_cases',
        'total_death',
        'total_recover',
        'active_cases',
        'total_case_per_minion_pop',
        'total_death_per_minion_pop',
        ]

class NewCasesForm(forms.ModelForm):
    class Meta:
        model=NewCases
        fields=[
        'new_cases',
        'new_death'
        ]
