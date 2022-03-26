from enum import unique
from django.db import models

# Create your models here.

class Movie(models.Model): # Ctrl - Control
    class TYPE:
        MOVIE = 'MOVIE'
        TRAILER = 'TRAILER'
        SHOW = 'SHOW'
        SERIES = 'SERIES'
        
        CHOICES = (
            (MOVIE, MOVIE),
            (TRAILER, TRAILER),
            (SHOW, SHOW),
            (SERIES, SERIES)
        )

    title = models.CharField(max_length=200)      # title VARCHAR(200)
    released_year = models.IntegerField(null=True)         # released_year INT
    language = models.CharField(max_length=50, default="O'zbek tili")
    duration = models.DurationField(max_length=50) 
    views_count = models.IntegerField(default=0)   # INT
    source_link = models.URLField(max_length=500)         # VARCHAR(500)
    created_at = models.DateTimeField(auto_now_add=True)  # TIMESTAMP "YYYY:MM:DD HH:MM:SS"
    modified_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=7, choices=TYPE.CHOICES,
                            default=TYPE.MOVIE)
    banner = models.ImageField(upload_to='banners', null=True) # VARCHAR(500)  -> banners/phone_acrIKBJ.jpg
    slug = models.SlugField(max_length=250)                           # VARCHAR
    category_id = models.IntegerField(null=True)

    # objects = models.Manager()

    def __str__(self):
        return self.title


titles = ["O'rgimchak odam", "Qasoskorlar 1", "Temir Odam 2"]
released_year = [2010, 2011, 2013]
duration = ['2 soat 10 min', '1 soatu 45 minut', '2 soatu 15 min']
source_link = ['uzmovi.uz/1', 'uzmovi.uz/2', 'uzmovi.uz/3']
slug = ['orgimchak-odam', 'qasoskorlar-1', 'temir-odam-2']

