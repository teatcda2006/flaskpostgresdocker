from db import Base, engine
from models.books import Author, Book

# Создаем все таблицы, описанные в моделях
Base.metadata.create_all(bind=engine)
