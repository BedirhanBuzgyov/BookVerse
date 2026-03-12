from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all().select_related("author").prefetch_related("genres")

    return render(request, "books/book_list.html", {"books": books})


def book_detail(request: HttpRequest, id) -> HttpResponse:
    book = get_object_or_404(
        Book.objects.select_related("author").prefetch_related("genres"),
        id=id,
    )

    return render(request, "books/book_detail.html", {"book": book})