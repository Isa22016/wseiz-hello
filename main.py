from library.book import Book
from library.member import Member
from library.librarian import Librarian
from library.library import Library

def main():
    # Create a library
    my_library = Library()

    # Add books
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    my_library.add_book(book1)
    my_library.add_book(book2)

    # Add members
    member1 = Member("Alice Smith", "1")
    member2 = Member("Bob Brown", "2")
    my_library.add_member(member1)
    my_library.add_member(member2)

    # Add a librarian
    librarian = Librarian("Charles Green", "1")
    
    # Display library details
    print(my_library)
    print(book1)
    print(member1)
    print(librarian)

if __name__ == "__main__":
    main()
