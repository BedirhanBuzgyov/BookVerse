from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Book

def book_list(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all().select_related("author").prefetch_related("genres")

    return render(request, "books/book_list.html", {"books": books})

