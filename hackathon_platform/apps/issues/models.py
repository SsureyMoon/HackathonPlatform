from django.db import models
from django.conf import settings

from core.models import TimeStampedModel
from core.utils import GenerateRandomFilename

generate_random_filename = GenerateRandomFilename('issues')

COUNTRY_CHOICES = (
	('US', 'United States'),
	('KR', 'KOREA, REPUBLIC OF'),
	('KH', 'Cambodia'),
	('VN', 'Viet Nam'),
	('ID', 'Indonesia'),
	('KE', 'KENYA'),
	('MY', 'Malaysia'),
	('TZ', 'TANZANIA'),
	('GG', 'Global'),
)

# Create your models here.
class Issue(TimeStampedModel):

	title = models.CharField(max_length=200)
	snippet = models.CharField(max_length=100)
	picture = models.ImageField(upload_to=generate_random_filename, blank=True, null=True)
	description = models.TextField()
	country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='GG')
	raiser = models.ForeignKey(settings.AUTH_USER_MODEL)