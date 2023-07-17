from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'
