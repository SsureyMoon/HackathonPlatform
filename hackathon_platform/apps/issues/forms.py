from django import forms

from .models import COUNTRY_CHOICES, Issue


class IssueCreateForm(forms.ModelForm):
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)
    picture = forms.ImageField()

    class Meta:
        model = Issue
        fields = ['title', 'snippet', 'country', 'description', 'picture']
