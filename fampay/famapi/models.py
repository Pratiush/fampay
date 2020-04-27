from django.db import models

# Create your models here.

class videoEntity(models.Model):
	title = models.CharField(max_length=500)
	description = models.CharField(max_length=1000)
	pub_date = models.DateTimeField('Date Published')
	thumbnail_url = models.CharField(max_length=500)

	def __str__(self):
		return self.title

	@classmethod
	def create(cls,title,description,pub_date,thumbnail_url):
		video = cls(title=title,description=description,pub_date=pub_date,thumbnail_url=thumbnail_url)
		return video
