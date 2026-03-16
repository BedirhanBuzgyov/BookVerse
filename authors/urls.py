from django.urls import path
from .views import *

urlpatterns = [
    path("", author_list, name="author_list"),
    path("add/", author_create, name="author_create"),
    path("<int:id>", author_detail, name="author_detail"),
    path("<int:id>/edit/", author_edit, name="author_edit"),
    path("<int:id>/delete/", author_delete, name="author_delete")

]