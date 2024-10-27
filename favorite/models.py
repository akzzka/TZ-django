from django.db import models
from django.conf import settings
from songs.models import Song  # Импорт модели Song

class Favorite(models.Model):
    """
    Модель Favorite связывает пользователя и песню,
    представляя избранные песни пользователя.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'song')  # Один пользователь может добавить песню в избранное только один раз

    def __str__(self):
        return f"{self.user.username} - {self.song.title}"
