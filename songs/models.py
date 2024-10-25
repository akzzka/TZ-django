from django.db import models
from artist.models import Artist
from genre.models import Genre

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name='songs', on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return self.title
