from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def book_list(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all().select_related("author").prefetch_related("genres")

    return render(request, "books/book_list.html", {"books": books})


def book_detail(request: HttpRequest, id) -> HttpResponse:
    book = get_object_or_404(
        Book.objects.select_related("author").prefetch_related("genres"),
        id=id,
    )

    return render(request, "books/book_detail.html", {"book": book})


def book_create(request: HttpRequest):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("book_detail", id=book.id)
    else:
        form = BookForm()

    return render(request, "books/book_form.html", {"form": form})