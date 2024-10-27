from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Favorite
from songs.models import Song
from .serializers import FavoriteSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления избранными песнями пользователя.
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращает избранные песни текущего пользователя
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Автоматически задает текущего пользователя в качестве автора избранного
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['POST'], url_path='add')
    def add_to_favorites(self, request, pk=None):
        # Добавление песни в избранное
        try:
            song = Song.objects.get(pk=pk)
            favorite, created = Favorite.objects.get_or_create(user=request.user, song=song)
            if created:
                return Response({"status": "Песня добавлена в избранное"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status": "Песня уже в избранном"}, status=status.HTTP_200_OK)
        except Song.DoesNotExist:
            return Response({"error": "Песня не найдена"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['DELETE'], url_path='remove')
    def remove_from_favorites(self, request, pk=None):
        # Удаление песни из избранного
        try:
            favorite = Favorite.objects.get(user=request.user, song__pk=pk)
            favorite.delete()
            return Response({"status": "Песня удалена из избранного"}, status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response({"error": "Песня не найдена в избранном"}, status=status.HTTP_404_NOT_FOUND)
