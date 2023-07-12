from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, content: str):
        self.title = title
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class WebFormatter(BaseFormatter):
    def format(self, book: Book):
        return f"{book.content}"


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}\n{book.content}"


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)


"""
class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book
"""
