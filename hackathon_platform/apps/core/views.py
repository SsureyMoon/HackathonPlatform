from django.shortcuts import render

# Create your views here.
from hackathons.models import Hackathon
from issues.models import Issue


def home(request):
	issues = Issue.objects.all()[:4]
	hackathons = Hackathon.objects.all()[:4]
	return render(request, 'home.html', { 'issues': issues, 'hackathons': hackathons })

def how_it_works(request):
	return render(request, 'howitworks.html')