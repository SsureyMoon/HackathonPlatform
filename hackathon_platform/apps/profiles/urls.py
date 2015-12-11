__author__ = 'ssureymoon'
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.UserAuthView.as_view(), name='login'),
	url(r'^signup/$', views.UserCreateView.as_view(), name='signup'),
]