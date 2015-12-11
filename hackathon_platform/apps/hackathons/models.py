from django.db import models
from django.conf import settings

from core.models import TimeStampedModel
from core.utils import GenerateRandomFilename
from issues.models import Issue

generate_random_filename = GenerateRandomFilename('hackathons')


class Hackathon(TimeStampedModel):

	title = models.CharField(max_length=200)
	snippet = models.CharField(max_length=100)
	picture = models.ImageField(upload_to=generate_random_filename, blank=True, null=True)
	description = models.TextField()
	due_date_time = models.DateTimeField()
	contribute_to = models.ForeignKey(Issue)
	host = models.ForeignKey(settings.AUTH_USER_MODEL)
