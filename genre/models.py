from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название жанра")
    description = models.TextField(blank=True, verbose_name="Описание жанра")

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genre"
        ordering = ['name']  # сортировка по названию

    def __str__(self):
        return self.name