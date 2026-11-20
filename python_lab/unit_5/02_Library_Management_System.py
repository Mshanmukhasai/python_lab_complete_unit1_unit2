class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C Programming"]

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("You borrowed:", book)
        else:
            print("Book is not available")

    def return_book(self, book):
        self.books.append(book)
        print("You returned:", book)


# Create library
library = Library()

# Display books
library.display_books()

# Borrow a book
library.borrow_book("Python")

# Return a book
library.return_book("Python")

# Display books again
library.display_books()