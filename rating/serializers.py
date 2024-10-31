from rest_framework import serializers

from rating.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    product = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = Rating
        fields = ('id','owner', 'song', 'ratings', 'product')
        read_only_fields = ('song',)