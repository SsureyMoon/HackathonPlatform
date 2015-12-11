from django import forms
from .models import Hackathon


class HackathonCreateForm(forms.ModelForm):
    picture = forms.ImageField()
    due_date = forms.DateField()
    due_time = forms.TimeField()

    class Meta:
        model = Hackathon
        fields = ['title', 'snippet', 'due_date', 'description', 'picture', 'due_time']

    def clean(self):
        print self.cleaned_data