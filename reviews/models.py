from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.IntegerField()
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["movie", "user"]

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"