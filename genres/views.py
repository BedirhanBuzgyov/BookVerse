from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from genres.forms import GenreForm
from genres.models import Genre


def genre_list(request):
    genres = Genre.objects.all()

    paginator = Paginator(genres, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "genres/genre_list.html", {
        "page_obj": page_obj,
    })

def genre_detail(request: HttpRequest, id) -> HttpResponse:
    genre = get_object_or_404(
        Genre, id=id
    )
    books = genre.book_set.all()

    context = {
        "genre": genre,
        "books": books,
    }

    return render(request, "genres/genre_detail.html", context)

def genre_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            return redirect("genre_detail", id=genre.id)
    else:
        form = GenreForm()

    return render(request, "genres/genre_form.html", {"form": form})

def genre_edit(request: HttpRequest, id) -> HttpResponse:
    genre = get_object_or_404(Genre, id=id)

    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect("genre_detail", id=genre.id)
    else:
        form = GenreForm(instance=genre)

    return render(request, "genres/genre_form.html", {"form": form, "genre": genre})

def genre_delete(request: HttpRequest, id):
    genre = get_object_or_404(Genre, id=id)

    if request.method == "POST":
        genre.delete()
        return redirect("genre_list")

    return render(request, "genres/genre_delete.html", {"genre": genre})