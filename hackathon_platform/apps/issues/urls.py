from django.conf.urls import url

from .views import IssueListView, IssueDetailView, IssueCreateView
from hackathons.views import HackathonCreateView


urlpatterns = [
	url(r'^$', IssueListView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', IssueDetailView.as_view(), name='detail'),
	url(r'^create/$', IssueCreateView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/hackathons/$', HackathonCreateView.as_view(), name='create_hackathon'),

]