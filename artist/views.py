from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from .models import Artist
from  .serializers import ArtistSerializer

class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'

class ArtistViewsSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = StandartResultPagination

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]

