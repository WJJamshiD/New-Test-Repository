# Generated by Django 3.2 on 2022-03-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('released_year', models.IntegerField(null=True)),
                ('language', models.CharField(default="O'zbek tili", max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('views_count', models.IntegerField(default=0)),
                ('source_link', models.URLField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('MOVIE', 'MOVIE'), ('TRAILER', 'TRAILER'), ('SHOW', 'SHOW'), ('SERIES', 'SERIES')], default='MOVIE', max_length=7)),
                ('banner', models.ImageField(upload_to='banners')),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]
