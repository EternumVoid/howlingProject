from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(max_length=450)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)
    uploaded = models.BooleanField(default=False)

    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploader')

    image = models.ImageField(upload_to='static/game_images', null=True, blank=True)
    users = models.ManyToManyField(User, related_name='users')

    def __str__(self):
        return f'{self.title}'
