
from django.contrib import admin
from .models import Genre, Book

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'display_genres', 'borrowed_by', 'borrow_date')  
    search_fields = ('title', 'author', 'borrowed_by')  
    list_filter = ('published_date', 'genres')  