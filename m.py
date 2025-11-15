class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookPrinter:
    def print_book(self, book):
        print(f"Title: {book.title}, Author: {book.author}")

b = Book("Python Basics", "John Doe")
printer = BookPrinter()
printer.print_book(b)
