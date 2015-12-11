from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, View
from django.contrib.auth import authenticate, login, logout

from profiles.models import User
from . import forms


# Create your views here.
class UserAuthView(View):

	def get(self, request):
		return render(request, "profiles/login.html", {'action':'login'})

	def post(self, request):

		form = AuthenticationForm(data=request.POST)

		if form.is_valid():
			print "hi"
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password']
			)

			if user is not None:
				login(request, user)
				return redirect('home')
		messages.error(request, "login failed")
		return render(request, "profiles/login.html", {'action':'login'})


class UserCreateView(View):

	def get(self, request):
		return render(request, "profiles/login.html", {'action':'signup'})

	def post(self, request):
		form = forms.RegistrationForm(request.POST)

		if form.is_valid():
			user = form.save()
			if user:
				user.backend = 'django.contrib.auth.backends.ModelBackend'
				login(request, user)
				messages.info(request, "signup success")
				return redirect("home")
		messages.error(request, "signup failed")
		return render(request, "profiles/login.html", {"action":"signup"})
