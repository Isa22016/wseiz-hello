from library.book import Book
from library.member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def __str__(self):
        return f"Library with {len(self.books)} books and {len(self.members)} members."
