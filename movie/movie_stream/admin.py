from django.contrib import admin
from .models import *
# Register your models here.
from django.db import models

admin.site.register(Movie)
admin.site.register(Comment)
