# Generated by Django 4.2.3 on 2023-07-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_game_description_alter_game_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='uploaded',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/game_images'),
        ),
    ]
