from django.shortcuts import render

from actors.models import Actor
from movies.models import Movie


def movie_detail_view(request, movie_id):
    selected_movie = Movie.objects.filter(id=movie_id).first()
    actors = selected_movie.actors.all()
    return render(request, 'moviedetail.html', {'movie': selected_movie, 'actors': actors})

