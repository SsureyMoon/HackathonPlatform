from django.contrib.auth.forms import UserCreationForm

__author__ = 'ssureymoon'
from django import forms
from profiles.models import User


class LoginForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'password']


class RegistrationForm(UserCreationForm):

	# confirm = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ["email", 'username',]

	# def clean_confirm(self):
	# 	if not self.cleaned_data['confirm']:
	# 		raise forms.ValidationError("Enter a confirm password.")
	# 	return self.cleaned_data['confirm']

