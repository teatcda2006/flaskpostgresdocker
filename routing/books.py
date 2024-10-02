from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db import get_db
from schemas.books import Book, BookCreate
from services.books import BookService
from depends import get_book_service

router = APIRouter(prefix="/books", tags=["books"])


@router.get("", response_model=List[Book])
async def get_all_books(db: Session = Depends(get_db),
                        book_service: BookService = Depends(get_book_service)):
    return book_service.get_books(db)


@router.get("/{id}", response_model=Book)
async def get_book(db: Session = Depends(get_db),
                   book_service: BookService = Depends(get_book_service), id: int = 0):
    book = book_service.get_book(db, id)
    if book is None:
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    return book


@router.post("", response_model=Book)
async def create_book(book: BookCreate, db: Session = Depends(get_db),
                      book_service: BookService = Depends(get_book_service)):
    return book_service.create_book(db, book, book.author)
