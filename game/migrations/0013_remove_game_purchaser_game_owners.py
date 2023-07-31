# Generated by Django 4.2.3 on 2023-07-25 14:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0012_remove_game_owned_game_purchaser_delete_ownership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='purchaser',
        ),
        migrations.AddField(
            model_name='game',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='owned_games', to=settings.AUTH_USER_MODEL),
        ),
    ]
