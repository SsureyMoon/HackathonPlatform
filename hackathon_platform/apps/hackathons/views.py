from django.shortcuts import render, get_object_or_404, redirect
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, View
from braces.views import LoginRequiredMixin

from .models import Hackathon
from .forms import HackathonCreateForm
from issues.models import Issue


class HackathonListView(ListView):
	model = Hackathon
	template_name = "hackathons/list.html"


class HackathonDetailView(View):

	def get(self, request, *args, **kwargs):
		hackathon = get_object_or_404(Hackathon, pk=kwargs['pk'])
		issue = hackathon.contribute_to
		return render(request, "hackathons/detail.html", {'hackathon': hackathon, 'issue': issue})


class HackathonCreateView(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		issue = get_object_or_404(Issue, pk=kwargs['pk'])
		form = HackathonCreateForm()
		return render(request, "hackathons/create.html", {'form': form, "issue": issue})

	def post(self, request, *args, **kwargs):
		issue = get_object_or_404(Issue, pk=kwargs['pk'])
		form = HackathonCreateForm(request.POST, request.FILES)
		
		is_vaild = form.is_valid()

		if is_vaild:

			due_date = form.cleaned_data['due_date']
			due_time = form.cleaned_data['due_time']

			hackathon = form.save(commit=False)
			hackathon.due_date_time = datetime.combine(due_date, due_time)
			hackathon.host = request.user
			hackathon.contribute_to = issue
			hackathon.save()
			return redirect("hackathons:detail", hackathon.pk)
		return redirect("hackathons:create")