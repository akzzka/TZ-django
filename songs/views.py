from rest_framework import generics
from .models import Song
from .serializers import SongSerializer
from rest_framework.pagination import PageNumberPagination

class SongListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongPagination(PageNumberPagination):
    page_size = 10 # количество элементов на странице
    page_size_query_param = 'page_size'  # позволяет клиенту устанавливать размер страницы
    max_page_size = 100
    
