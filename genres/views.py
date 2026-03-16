from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from genres.models import Genre


def genre_list(request: HttpRequest) -> HttpResponse:
    genres = Genre.objects.all()
    return render(request, "genres/genre_list.html", {"genres": genres})

def genre_detail(request: HttpRequest, id) -> HttpResponse:
    genre = get_object_or_404(
        Genre, id=id
    )

    return render(request, "genres/genre_detail.html", {"genre": genre})
