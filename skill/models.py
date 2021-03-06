from django.db import models

# Create your models here.

class skill(models.Model):
	image = models.ImageField(upload_to='skillImage/')
	title = models.CharField(max_length=50, blank=False)
	descipt = models.TextField(max_length=500, blank=True)
	dateTime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def summary(self):
		return  self.descipt[0:100]

class ContactInfo(models.Model):

	cName = models.CharField(max_length=50)
	cEmail = models.CharField(max_length=50)
	cComment = models.TextField(max_length=1000)

	def __str__(self):
		return self.cName
	