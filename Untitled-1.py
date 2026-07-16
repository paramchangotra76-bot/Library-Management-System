class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {status}"


class Library:
    def __init__(self):
        self.books = []
        self.load_sample_books()

    def load_sample_books(self):
        sample_books = [
            Book("Python Crash Course", "Eric Matthes", "9781593279288"),
            Book("Automate the Boring Stuff with Python", "Al Sweigart", "9781593279929"),
            Book("Clean Code", "Robert C. Martin", "9780132350884"),
            Book("The Pragmatic Programmer", "Andrew Hunt", "9780201616224"),
            Book("Introduction to Algorithms", "Thomas H. Cormen", "9780262033848"),
        ]
        self.books.extend(sample_books)

    def add_book(self, title, author, isbn):
        if self.find_book_by_isbn(isbn):
            print("A book with this ISBN already exists.")
            return
        self.books.append(Book(title, author, isbn))
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def search_book(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword == book.isbn:
                print(book)
                found = True
        if not found:
            print("No matching book found.")

    def issue_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if not book:
            print("Book not found.")
        elif not book.available:
            print("Book is already issued.")
        else:
            book.available = False
            print(f"You have issued: {book.title}")

    def return_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if not book:
            print("Book not found.")
        elif book.available:
            print("Book was not issued.")
        else:
            book.available = True
            print(f"You have returned: {book.title}")


def menu():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. View all books")
        print("2. Add a book")
        print("3. Search a book")
        print("4. Issue a book")
        print("5. Return a book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.view_books()

        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == "3":
            keyword = input("Enter title, author, or ISBN: ")
            library.search_book(keyword)

        elif choice == "4":
            isbn = input("Enter ISBN to issue: ")
            library.issue_book(isbn)

        elif choice == "5":
            isbn = input("Enter ISBN to return: ")
            library.return_book(isbn)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()