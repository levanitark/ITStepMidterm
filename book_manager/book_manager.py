# Project 3: Book Management App (OOP)
# add books, show all, search by title
# books get saved in books.json

import json
import os

# keep books.json in the same folder as this script
DATA_FILE = os.path.join(os.path.dirname(__file__), "books.json")


class Book:
    def __init__(self, title, author, year):
        # encapsulation - private attributes
        self._title = title
        self._author = author
        self._year = year

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    def display(self):
        return f'"{self._title}" by {self._author} ({self._year})'

    def to_dict(self):
        # turns the book into a dict for json
        return {
            "type": "book",
            "title": self._title,
            "author": self._author,
            "year": self._year,
        }


# inheritance - EBook inherits from Book
class EBook(Book):
    def __init__(self, title, author, year, file_format):
        super().__init__(title, author, year)
        self._file_format = file_format

    # polymorphism - overriding display()
    def display(self):
        return f'"{self.title}" by {self.author} ({self.year}) [E-Book, {self._file_format}]'

    def to_dict(self):
        return {
            "type": "ebook",
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "file_format": self._file_format,
        }


class BookManager:
    def __init__(self):
        self._books = []
        self.load_from_file()

    def add_book(self, book):
        # don't add the same book twice
        for existing in self._books:
            if (existing.title.lower() == book.title.lower()
                    and existing.author.lower() == book.author.lower()
                    and existing.year == book.year):
                print("This book is already in the list!")
                return
        self._books.append(book)
        self.save_to_file()
        print("Book added successfully!")

    def show_all(self):
        if len(self._books) == 0:
            print("The list is empty. Add some books first!")
            return

        print(f"\n--- All books ({len(self._books)}) ---")
        for number, book in enumerate(self._books, start=1):
            print(f"{number}. {book.display()}")

    def search_by_title(self, search_text):
        found = []
        for book in self._books:
            # lower() so the search ignores upper/lower case
            if search_text.lower() in book.title.lower():
                found.append(book)

        if len(found) == 0:
            print(f'No books found with title containing "{search_text}".')
        else:
            print(f"\n--- Found {len(found)} book(s) ---")
            for book in found:
                print(book.display())

    # saving to json file
    def save_to_file(self):
        books_as_dicts = [book.to_dict() for book in self._books]
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(books_as_dicts, file, indent=4, ensure_ascii=False)

    # loading from json file
    def load_from_file(self):
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            books_as_dicts = json.load(file)

        for data in books_as_dicts:
            if data["type"] == "ebook":
                book = EBook(data["title"], data["author"], data["year"], data["file_format"])
            else:
                book = Book(data["title"], data["author"], data["year"])
            self._books.append(book)

    # deleting the file
    def delete_data_file(self):
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)
            self._books = []
            print("All data deleted!")
        else:
            print("There is no data file to delete.")


def get_year():
    # validation for the year
    while True:
        try:
            year = int(input("Enter the year of publication: "))
            if 0 < year <= 2100:
                return year
            print("Please enter a realistic year!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def get_non_empty_text(prompt):
    # validation - text can't be empty
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("Input cannot be empty!")


def add_book_menu(manager):
    # asks the user for book info and adds it
    title = get_non_empty_text("Enter the title: ")
    author = get_non_empty_text("Enter the author: ")
    year = get_year()

    is_ebook = input("Is it an e-book? (yes/no): ").lower()
    if is_ebook == "yes":
        file_format = get_non_empty_text("Enter the file format (PDF, EPUB...): ")
        manager.add_book(EBook(title, author, year, file_format))
    else:
        manager.add_book(Book(title, author, year))


def main():
    manager = BookManager()
    print("=== Book Management Application ===")

    while True:
        print("\n1. Add a new book")
        print("2. Show all books")
        print("3. Search book by title")
        print("4. Delete all data")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_book_menu(manager)
        elif choice == "2":
            manager.show_all()
        elif choice == "3":
            search_text = get_non_empty_text("Enter the title to search: ")
            manager.search_by_title(search_text)
        elif choice == "4":
            manager.delete_data_file()
        elif choice == "5":
            break
        else:
            print("Invalid option! Please choose 1-5.")


if __name__ == "__main__":
    main()
