# Generated by Django 3.2 on 2022-03-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category_id',
            field=models.IntegerField(null=True),
        ),
    ]
