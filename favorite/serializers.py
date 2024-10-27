from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    """
    Сериализатор для избранных песен пользователя.
    """
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'song', 'created_at']
        read_only_fields = ['user', 'created_at']
