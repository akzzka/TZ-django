from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewsSet

router = DefaultRouter()
router.register(r'artist', ArtistViewsSet)

urlpatterns = [
    path('', include(router.urls)),  # Включите маршруты из роутера
]
