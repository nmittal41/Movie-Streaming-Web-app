from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class Movie(models.Model):
    title = models.CharField(max_length = 40, blank = False)
    desription = models.TextField(max_length = 500, blank = False)
    url = EmbedVideoField()

class Comment(models.Model):
    post = models.ForeignKey(Movie ,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,db_column = 'user')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)
