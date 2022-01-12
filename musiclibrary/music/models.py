from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50, null=False)
    artist = models.CharField(max_length=50, null=False)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    likes = models.IntegerField()
   