from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_likes_count(self, obj):
        return obj.likes.count()