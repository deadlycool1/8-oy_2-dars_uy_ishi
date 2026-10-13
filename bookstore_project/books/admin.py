from django.contrib import admin
from .models import Genre, Book

admin.site.register(Genre)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "price")
    list_filter = ("genre",)
    search_fields = ("title", "author")
