__author__ = 'ssureymoon'
from django.conf.urls import url

from .views import HackathonListView, HackathonDetailView, HackathonCreateView


urlpatterns = [
	url(r'^$', HackathonListView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', HackathonDetailView.as_view(), name='detail'),
]