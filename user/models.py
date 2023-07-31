from django.contrib.auth.models import User, AbstractUser
from django.db import models
from game.models import Game


class Library(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Library"
