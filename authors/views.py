from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Author

def author_list(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.all()
    return render(request, "authors/author_list.html", {"authors": authors})

def author_detail(request: HttpRequest, id) -> HttpResponse:
    author = get_object_or_404(
        Author, id=id
    )
    books = author.book_set.all()

    return render(request, "authors/author_detail.html")


