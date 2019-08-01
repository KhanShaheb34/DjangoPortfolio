from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='')
    title = models.TextField(max_length=150)
    summary = models.TextField(max_length=300)
    started = models.DateField()
    ended = models.DateField()
    assignedTo = models.TextField(max_length=150)
