import os
from peewee import *
from orm import Book, Author

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("Library Management System")
    print("-------------------------")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. View All Books")
    print("4. Find Book by Title")
    print("5. Add Author")
    print("6. Delete Author")
    print("7. View All Authors")
    print("8. Find Author by Name")
    print("9. Exit")

def add_book():
    clear_screen()
    title = input("Enter the title of the book: ")
    author_name = input("Enter the name of the author: ")
    genre = input("Enter the genre of the book: ")

    author, created = Author.get_or_create(name=author_name)

    Book.create(title=title, author=author, genre=genre)
    print("Book added successfully.")

def delete_book():
    clear_screen()
    title = input("Enter the title of the book to delete: ")
    book = Book.get_or_none(title=title)
    if book:
        book.delete_instance()
        print("Book deleted successfully.")
    else:
        print("Book not found.")

def view_all_books():
    clear_screen()
    print("All Books:")
    for book in Book.select():
        print(f"{book.title} by {book.author.name} - {book.genre} ({'Available' if book.available else 'Not Available'})")

def find_book_by_title():
    clear_screen()
    title = input("Enter the title of the book to find: ")
    book = Book.get_or_none(title=title)
    if book:
        print(f"{book.title} by {book.author.name} - {book.genre} ({'Available' if book.available else 'Not Available'})")
    else:
        print("Book not found.")

def add_author():
    clear_screen()
    name = input("Enter the name of the author: ")
    Author.create(name=name)
    print("Author added successfully.")

def delete_author():
    clear_screen()
    name = input("Enter the name of the author to delete: ")
    author = Author.get_or_none(name=name)
    if author:
        author.delete_instance()
        print("Author deleted successfully.")
    else:
        print("Author not found.")

def view_all_authors():
    clear_screen()
    print("All Authors:")
    for author in Author.select():
        print(author.name)

def find_author_by_name():
    clear_screen()
    name = input("Enter the name of the author to find: ")
    author = Author.get_or_none(name=name)
    if author:
        print(f"Author found: {author.name}")
    else:
        print("Author not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            delete_book()
        elif choice == '3':
            view
