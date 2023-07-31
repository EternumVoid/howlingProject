# Generated by Django 4.2.3 on 2023-07-25 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0011_remove_game_purchaser_game_owned_ownership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='owned',
        ),
        migrations.AddField(
            model_name='game',
            name='purchaser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Ownership',
        ),
    ]