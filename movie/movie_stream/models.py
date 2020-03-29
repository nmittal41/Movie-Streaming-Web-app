from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Movie(models.Model):
	title=models.CharField(max_length=30)
	description=models.TextField(max_length=300)
	path=models.CharField(max_length=80)
	datetime=models.DateTimeField(default=timezone.now)

class Comment(models.Model):
	text=models.TextField(max_length=300)
	datetime=models.DateTimeField(default=timezone.now)
	user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
	movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
