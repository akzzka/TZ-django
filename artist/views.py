from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Artist
from  .serializers import ArtistSerializer

class ArtistViewsSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]

