from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	text = models.TextField()
	image = models.ImageField(upload_to='blog/images/', blank=True)
	url = models.URLField(blank=True)

	def __str__(self):
		return self.title
