from django.urls import path
from .views import GenreListCreateView, BookListCreateView

urlpatterns = [
    path("genres/", GenreListCreateView.as_view(), name="genre-list-create"),
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
]
