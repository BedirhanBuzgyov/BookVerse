from django.urls import path

from genres.views import *

urlpatterns = [
    path("", genre_list, name="genre_list"),
    path("add/", genre_create, name="genre_create"),
    path("<int:id>/", genre_detail, name="genre_detail"),
    path("<int:id>/edit/", genre_edit, name="genre_edit"),
    path("<int:id>/delete/", genre_delete, name="genre_delete")
]