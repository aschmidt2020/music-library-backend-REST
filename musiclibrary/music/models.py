from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50, null=False)
    artist = models.CharField(max_length=50, null=False)
    album = models.CharField(max_length=50)
    album_art = models.ImageField(upload_to='images/', null=True)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    likes = models.IntegerField()
    
    def __str__(self):
        return self.title + ' ' + self.artist
   