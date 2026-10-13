from rest_framework import generics
from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        qs = Book.objects.select_related("genre")
        genre_id = self.request.query_params.get("genre")
        if genre_id:
            qs = qs.filter(genre_id=genre_id)
        return qs
