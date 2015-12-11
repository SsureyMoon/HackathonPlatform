__author__ = 'ssureymoon'
import os
from uuid import uuid4

from django.utils.deconstruct import deconstructible


@deconstructible
class GenerateRandomFilename(object):

	def __init__(self, sub_path):
		self.path = sub_path

	def __call__(self, instance, filename):
		ext = filename.split('.')[-1]
		# set filename as random string
		filename = '{}.{}'.format(uuid4().hex, ext)
		# return the whole path to the file
		return os.path.join(self.path, filename)
