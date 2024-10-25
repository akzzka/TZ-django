from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ArtistViewsSet

router = DefaultRouter()
router.register('', ArtistViewsSet)

urlpatterns = [
    path('', include(router.urls)),

     ]
