from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.select_related("user", "movie")
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        movie_id = self.request.query_params.get("movie")

        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)

        return queryset