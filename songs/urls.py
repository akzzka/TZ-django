from django.urls import path, include
from .views import SongListCreate, SongDetail, SongViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('songs/', SongListCreate.as_view(), name='song-list-create'),  # Список и создание песен
    # path('songs/<int:pk>/', SongDetail.as_view(), name='song-detail'),  # Получение, обновление и удаление песни
]
