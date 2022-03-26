from django.urls import path, include
from movies.views import movies_list, movie_detail, movie_create


urlpatterns = [
    path('', movies_list), # movies/hello
    path('<int:movie_id>', movie_detail), # movies/<int:id>   <- movies/10, movies/4, movies/100
    path('create', movie_create)
]
