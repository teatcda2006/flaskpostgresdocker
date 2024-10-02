from sqlalchemy.orm import Session
from models.books import Book, Author
from schemas.books import BookCreate, AuthorCreate


class BookRepository:

    def get_books(self, db: Session):
        return db.query(Book).all()

    def get_book(self, db: Session, id):
        return db.query(Book).filter(Book.id == id).first()

    def create_book(self, db: Session, book: BookCreate, author: AuthorCreate):
        db_author = Author(name=author.name)
        db.add(db_author)
        db.commit()
        db.refresh(db_author)

        db_book = Book(title=book.title, description=book.description, author_id=db_author.id)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
