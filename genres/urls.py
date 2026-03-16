from django.urls import path

from genres.views import *

urlpatterns = [
    path("", genre_list, name="genre_list"),
    path("<int:id>", genre_detail, name="genre_detail")
]