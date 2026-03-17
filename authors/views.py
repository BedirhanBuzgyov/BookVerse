from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AuthorForm
from .models import Author

def author_list(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.all()
    return render(request, "authors/author_list.html", {"authors": authors})

def author_detail(request: HttpRequest, id) -> HttpResponse:
    author = get_object_or_404(
        Author, id=id
    )
    books = author.book_set.all()
    context = {
        "author": author,
        "books": books,
    }

    return render(request, "authors/author_detail.html", context)

def author_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect("author_detail", id=author.id)
    else:
        form = AuthorForm()

    return render(request, "authors/author_form.html", {"form": form})

def author_edit(request: HttpRequest, id) -> HttpResponse:
    author = get_object_or_404(Author, id=id)

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect("author_detail", id=author.id)
    else:
        form = AuthorForm(instance=author)

    return render(request, "authors/author_form.html", {"form": form, "author": author})

def author_delete(request: HttpRequest, id) -> HttpResponse:
    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect("author_list")