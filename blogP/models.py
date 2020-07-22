from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=255)
	publish_date=models.DateTimeField()
	body=models.TextField()
	image = models.ImageField(upload_to='images/')
	def __str__(self):
		return self.title
	def summary(self):
		return self.body[:100]

	def publish_date_neat(self):
		return self.publish_date.strftime('%b %e %Y')