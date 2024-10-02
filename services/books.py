from typing import List
from sqlalchemy.orm import Session
from repositories.books import BookRepository
from schemas.books import Book, BookCreate, AuthorCreate


class BookService:

    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def get_books(self, db: Session) -> List[Book]:
        return self.repository.get_books(db)

    def get_book(self, db: Session, id) -> Book:
        return self.repository.get_book(db, id)

    def create_book(self, db: Session, book: BookCreate, author: AuthorCreate) -> Book:
        return self.repository.create_book(db, book, author)

