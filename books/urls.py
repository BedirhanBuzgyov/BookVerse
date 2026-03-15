from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("add/", views.book_create, name="book_create"),
    path("<int:id>/", views.book_detail, name="book_detail"),
    path("<int:id>/edit/", views.book_edit, name="book_edit"),
    path("<int:id>/delete/", views.book_delete, name="book_delete"),
]