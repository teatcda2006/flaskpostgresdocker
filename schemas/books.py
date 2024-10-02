from datetime import datetime
from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    description: str


class BookCreate(BookBase):
    author: AuthorCreate


class Book(BookBase):
    id: int
    author: Author

    class Config:
        orm_mode = True
