from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50, null=False)
    artist = models.CharField(max_length=50, null=False)
    album = models.CharField(max_length=50, null=True)
    album_art_link = models.TextField(max_length=None, null=True)
    genre = models.CharField(max_length=50, null=True)
    release_date = models.DateField(null=True)
    likes = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title + ' ' + self.artist
   