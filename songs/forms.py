from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'release_date', 'genre', 'audio_file']
        