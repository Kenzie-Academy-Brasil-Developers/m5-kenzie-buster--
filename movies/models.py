from django.db import models
from accounts.models import User


class RatingChoices(models.TextChoices):
    A = "PG"
    B = "PG-13"
    C = "R"
    D = "NC-17"
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=RatingChoices.choices,
        default=RatingChoices.DEFAULT,
    )
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )
    orders = models.ManyToManyField(
        User, through="MovieOrder", related_name="movie_orders")


class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
