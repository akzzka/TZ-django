from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Genre
from .serializers import GenreSerializers

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers

    # Настройка разрешений
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # Только администраторы могут изменять или удалять жанры
            self.permission_classes = [IsAdminUser]
        else:
            # Все аутентифицированные пользователи могут видеть жанры
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
