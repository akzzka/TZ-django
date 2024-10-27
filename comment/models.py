from django.db import models
from songs.models import Song
from django.conf import settings


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    Song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name='comments'
    )


    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Использование модели пользователя из настроек
        on_delete=models.CASCADE,
        related_name='comments'
    )
