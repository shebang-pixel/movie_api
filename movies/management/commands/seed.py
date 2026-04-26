from django.core.management.base import BaseCommand
from movies.models import Movie
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.first()

        Movie.objects.create(
            title="Seed Movie",
            slug="seed-movie",
            genre="action",
            year=2024,
            user=user
        )

        print("Seeded!")