from django.db import models
#from django.db.models.loading import get_model

# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title