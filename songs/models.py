from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True)
    release_date = models.DateField()
    genre = models.CharField(max_length=50, blank=True)
    audio_file = models.FileField(upload_to='song/')

    def __str__(self) -> str:
        return f'{self.title}, {self.artist}'
    