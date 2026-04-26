from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    year = models.IntegerField()

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    likes = models.ManyToManyField(
        User,
        related_name="liked_movies",
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title