
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def display_all_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("All Books in the Library:")
            for book in self.books:
                print(book)

    def search_book_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if not found_books:
            print(f"No books found with the title '{title}'.")
        else:
            print(f"Found {len(found_books)} book(s) with the title '{title}':")
            for book in found_books:
                print(book)


# Example usage:
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
book3 = Book("1984", "George Orwell", "978-0451524935")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_all_books()

library.search_book_by_title("To Kill a Mockingbird")
library.search_book_by_title("Harry Potter")

