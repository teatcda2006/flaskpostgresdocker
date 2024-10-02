from repositories.books import BookRepository
from services.books import BookService

book_repository = BookRepository()
book_service = BookService(book_repository)


def get_book_service() -> BookService:
    return book_service
