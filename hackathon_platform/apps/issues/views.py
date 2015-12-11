from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DetailView, View

from braces.views import LoginRequiredMixin

from .models import Issue, COUNTRY_CHOICES
from .forms import IssueCreateForm


class IssueActionMixin(object):

	@property
	def success_msg(self):
		return NotImplemented

	def form_valid(self, form):
		messages.info(self.request, self.success_msg)
		return super(IssueActionMixin, self).form_valid(form)


class IssueCreateView(LoginRequiredMixin, IssueActionMixin, View):
	success_msg = "Created"

	def get(self, request):
		form = IssueCreateForm()
		return render(request, "issues/create.html", {'form': form})

	def post(self, request):
		form = IssueCreateForm(request.POST, request.FILES)

		if form.is_valid():
			issue = form.save(commit=False)
			issue.raiser = request.user
			issue.save()
			return redirect("issues:detail", issue.pk)
		return redirect("issues:create")



class IssueListView(ListView):
	model = Issue
	template_name = "issues/list.html"

	def get_queryset(self):
		queryset = super(IssueListView, self).get_queryset()

		q = self.request.GET.get('q')
		if q:
			return queryset.filter(title__icontains=q)
		return queryset

class IssueDetailView(IssueActionMixin, View):
	success_msg = "Updated"

	def get(self, request, *args, **kwargs):
		issue = get_object_or_404(Issue, pk=kwargs['pk'])
		return render(request, "issues/detail.html", {'issue': issue})

