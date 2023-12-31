# Generated by Django 4.2.3 on 2023-07-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/game_images'),
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
