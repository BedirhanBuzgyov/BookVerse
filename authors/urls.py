from django.urls import path
from .views import *

urlpatterns = [
    path("", author_list, name="author_list"),
    path("<int:id>", author_detail, name="author_detail")
]