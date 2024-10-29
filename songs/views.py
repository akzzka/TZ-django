from rest_framework import generics
from .models import Song
from .serializers import SongSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rating.serializers import RatingSerializer
from rest_framework.response import Response


class SongListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    @action(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'], detail=True)
    def rating(self,request, pk):
        song = self.get_object()
        user = request.user

        if request.method == 'GET':
            ratings = song.ratings.all()
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data, status=200)

        elif request.method == 'POST':
            serizlizer = RatingSerializer(data=request.data)
            serizlizer.is_valid(raise_exception=True)
            serizlizer.save(owner=user, song=song)
            return Response(serizlizer.data, status=201)

        elif request.method in ['PUT', 'PATCH']:
            if not song.ratings.filter(owner=user).exists():
                return Response( 'Вы не оставляли рейтинг на этот товар', status=404)
            rating = song.ratings.get(owner=user)
            serializer = RatingSerializer(rating, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)

        else:
            if not song.ratings.filter(owner=user).exists():
                return Response('Вы не оставляли рейтинг на этот товар', status=404)
            rating = song.ratings.get(owner=user)
            rating.delete()
            return Response('Удалено',status=204)
