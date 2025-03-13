from ninja import NinjaAPI, Router
from django.shortcuts import get_object_or_404
from .models import Book, Genre
from datetime import datetime
from typing import List, Dict, Optional

api = NinjaAPI(version="1.0", urls_namespace="library_api")
router = Router()

# --------------------- BOOKS API ---------------------

@router.get("/books", response=List[Dict])
def get_books(request, genre: Optional[str] = None, borrowed_by: Optional[str] = None, borrowed: Optional[bool] = None):
    qs = Book.objects.all()

    if genre:
        qs = qs.filter(genres__name__icontains=genre)  
    if borrowed_by:
        qs = qs.filter(borrowed_by__icontains=borrowed_by)  

    if borrowed is not None:
        if borrowed:
            qs = qs.exclude(borrowed_by__isnull=True).exclude(borrowed_by="")
        else:
            qs = qs.filter(borrowed_by__isnull=True) | qs.filter(borrowed_by="")  

    return list(qs.values())

@router.get("/books/{book_id}", response=Dict)
def get_book_detail(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return {"id": book.id, "title": book.title, "author": book.author, "published_date": book.published_date}

@router.post("/books", response=Dict)
def create_book(request, title: str, author: str, published_date: str, genres: List[int]):
    book = Book.objects.create(title=title, author=author, published_date=datetime.strptime(published_date, "%Y-%m-%d"))
    book.genres.set(genres)
    return {"message": "Book created successfully", "book_id": book.id}

@router.post("/books/{book_id}/borrow/", response=Dict)
def borrow_book(request, book_id: int, borrowed_by: str):
    book = get_object_or_404(Book, id=book_id)

    if book.borrowed_by:
        return {"error": "Book is already borrowed"}

    book.borrowed_by = borrowed_by
    book.borrow_date = datetime.now()
    book.save()

    return {"message": f"Book '{book.title}' borrowed by {borrowed_by}"}

api.add_router("/api", router)

# --------------------- GENRES API ---------------------

@router.get("/genres", response=List[Dict])
def get_genres(request):
    return list(Genre.objects.values())

@router.post("/genres", response=Dict)
def create_genre(request, name: str, description: Optional[str] = None):
    genre = Genre.objects.create(name=name, description=description or "")
    return {"message": "Genre created successfully", "genre_id": genre.id}

@router.put("/genres/{id}", response=Dict)
def update_genre(request, id: int, name: Optional[str] = None, description: Optional[str] = None):
    genre = get_object_or_404(Genre, id=id)

    if name:
        genre.name = name
    if description:
        genre.description = description

    if name or description:
        genre.save()
        return {"message": "Genre updated successfully"}

    return {"error": "No changes provided"}

@router.delete("/genres/{id}", response=Dict)
def delete_genre(request, id: int):
    genre = get_object_or_404(Genre, id=id)
    genre.delete()
    return {"message": "Genre deleted successfully"}
