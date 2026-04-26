from rest_framework.viewsets import ModelViewSet
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.select_related("user").prefetch_related("likes")
    serializer_class = MovieSerializer
    
    # Permissions
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    # Search
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["title", "genre"]
    
    # 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    # custom action
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        movie = self.get_object()
        movie.likes.add(request.user)

        return Response({"message": "liked"})
    
    # get movie reviews
    @action(detail=True, methods=["get"])
    def reviews(self, request, pk=None):
        movie = self.get_object()
        reviews = movie.reviews.select_related("user")

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)