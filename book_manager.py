import json
import random
from datetime import datetime
from file_handler import load_books, save_books

def add_book():
    books = load_books()

    title = input("Enter book title: ")
    author = input("Enter author(s): ")
    isbn = str(random.randint(10000, 99999))  # Generate a random 5-digit number
    year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,  # Automatically generated
        "year": year,
        "price": price,
        "quantity": quantity,
        "lent": 0  # Tracks how many books are lent
    }
    books.append(book)
    save_books(books)
    print(f'Book "{title}" added successfully with ISBN {isbn}.')

def view_books():
    books = load_books()
    if not books:
        print("No books available.")
        return
    print("\nAvailable Books:")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. {book['title']} by {book['author']} (ISBN: {book['isbn']}) - {book['quantity']} in stock, {book['lent']} lent")

def update_book():
    books = load_books()
    title = input("Enter the title of the book to update: ")
    for book in books:
        if book["title"].lower() == title.lower():
            print("Book found. Update details below (leave blank to skip):")
            book["author"] = input(f"Author(s) [{book['author']}]: ") or book["author"]
            book["year"] = input(f"Publishing Year [{book['year']}]: ") or book["year"]
            book["price"] = float(input(f"Price [{book['price']}]: ") or book["price"])
            book["quantity"] = int(input(f"Quantity [{book['quantity']}]: ") or book["quantity"])
            book["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_books(books)
            print(f'Book "{title}" updated successfully.')
            return
    print("Book not found.")

def remove_book():
    books = load_books()
    title = input("Enter the title of the book to remove: ")
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print(f'Book "{title}" removed successfully.')
            return
    print("Book not found.")
