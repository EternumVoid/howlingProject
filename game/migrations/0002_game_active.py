# Generated by Django 4.2.3 on 2023-07-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
