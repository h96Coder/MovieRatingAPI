from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    movie_name = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.movie_name


class Rating(models.Model):
    choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=choices, default=1)
    rater = models.ForeignKey(User, on_delete=models.DO_NOTHING)


# Create your models here.
