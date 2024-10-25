from django.urls import path
from .views import SongListCreate, SongDetail

urlpatterns = [
    path('songs/', SongListCreate.as_view(), name='song-list-create'),  # Список и создание песен
    path('songs/<int:pk>/', SongDetail.as_view(), name='song-detail'),  # Получение, обновление и удаление песни
]
