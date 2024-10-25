from rest_framework import  serializers

from genre .models import Genre

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'