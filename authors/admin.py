from django.contrib import admin

from authors.models import Author
from books.models import Book
from genres.models import Genre


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ...

@admin.register(Genre)
class ModelNameAdmin(admin.ModelAdmin):
    ...