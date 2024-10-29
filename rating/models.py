from django.db import models
from  django.contrib.auth import get_user_model

from songs.models import Song

User = get_user_model()

class Rating(models.Model):
    RATING_CHOICE = (
        (1,'Too Bad'),
        (2, 'Bad'),
        (3, 'Good'),
        (4, 'Nice'),
        (5, 'Perfect')
    )
    song = models.ForeignKey(Song,on_delete=models.CASCADE, related_name='ratings')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ratings')
    ratings = models.PositiveSmallIntegerField(choices=RATING_CHOICE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['owner','song']
