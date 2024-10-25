from django.db import models
from account.models import CustomUser


class Artist(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artist/')

    def __str__(self):
        return f'{self.name} | Место рождения: {self.city}'

class Meta:
    verbose_name = 'Artist'
    verbose_name_plural = 'Artists'
