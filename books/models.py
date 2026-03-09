from django.db import models
from authors.models import Author
from genres.models import Genre


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title