from typing import List, Union


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, book_title) -> Union[Book, str]:
        try:
            return [b for b in self.books if b.title == book_title][0]
        except ValueError:
            return "Book does not exist"


"""
class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page

"""


