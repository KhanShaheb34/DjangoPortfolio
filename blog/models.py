from django.db import models

# Create your models here.

class Post(models.Model):
    thumbnail = models.ImageField(upload_to='')
    title = models.TextField(max_length=150)
    content = models.TextField()
    dateCreated = models.DateField()