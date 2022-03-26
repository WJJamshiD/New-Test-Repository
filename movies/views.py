from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from movies.models import Movie



def movies_list(request): 
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie_list.html', context) # response


def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id) # get(title='')
    except Exception as e:
        print(e)
        raise Http404('Bunday sahifa topilmadi')

    context = {
        'movie': movie,
    }
    return render(request, 'movie_detail.html', context)


def movie_create(request):
    # request.GET
    errors = {}
    data = {}
    
    if request.method == 'POST': # data = reuqest.POST : dict
        print(request.POST) # <QueryDict: {'title': ['asdasd'], 'released_year': ['234234'], 'language': ['english'], 'duration': [''], 'source_link': [''], 'type': ['SERIES'], 'csrfmiddlewaretoken': ['LJKe3tJW3HrWrJlf8FPrcC0P9BL5j8jujtxoQmD1McLn8guWniqx4SGq7KlBMV4F'], 'banner': [''], 'slug': ['fantastika']}>
        title = request.POST.get('title') # 'asdasd'
        released_year = request.POST.get('released_year')
        lang = request.POST.get('language')
        duration = request.POST.get('duration')
        source_link = request.POST.get('source_link')
        type = request.POST.get('type')
        slug = request.POST.get('slug')
        
        if not title:
            errors['title'] = 'Iltimos title ni kiriting'
        if not duration:
            errors['duration'] = 'Iltimos duration qiymatini kiriting'
        if not type in ['MOVIE', "TRAILER", "SERIES", "SHOW"]:
            errors['type'] = 'Siz tanlagan tur bizning variantlarimiz orasida yo\'q'
        
        if len(errors) == 0:
            new_movie = Movie(title=title,language=lang,
                    duration=duration, source_link=source_link, type=type, slug=slug)
            # slug = 'asdkjaskdasd'
            # new_movie.slug = slug
            if released_year:
                new_movie.released_year = released_year
            new_movie.save()
            # new_movie = Movie.objects.create(
            #     title=title, released_year=released_year, language=lang,
            #     duration=duration, source_link=source_link, type=type
            # )
            # return render(request, "movie_create_finish.html", {})
            return redirect('/movies/') # localhost:8001/movies/  # absolute url | relative url
        else:
            data = {
                'title': title,
                'released_year': released_year,
                'language': lang,
                'duration': duration,
                'source_link': source_link,
                'type': type,
                'slug': slug
            }

    context = {'errors': errors, 'data': data}
    return render(request, 'movies/movie_create.html', context)