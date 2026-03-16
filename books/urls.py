from django.urls import path
from .views import *

urlpatterns = [
    path("", book_list, name="book_list"),
    path("add/", book_create, name="book_create"),
    path("<int:id>/", book_detail, name="book_detail"),
    path("<int:id>/edit/", book_edit, name="book_edit"),
    path("<int:id>/delete/", book_delete, name="book_delete"),
]