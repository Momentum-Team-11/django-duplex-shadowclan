# Generated by Django 4.0.3 on 2022-03-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcardsapp', '0008_alter_flashcard_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='card_seen',
            field=models.BooleanField(default=False),
        ),
    ]