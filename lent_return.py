from file_handler import load_books, save_books

def lend_book():
    books = load_books()
    title = input("Enter the title of the book to lend: ")
    for book in books:
        if book["title"].lower() == title.lower():
            if book["quantity"] > book["lent"]:
                book["lent"] += 1
                save_books(books)
                print(f'Book "{title}" lent successfully.')
                return
            else:
                print(f'No available copies of "{title}" to lend.')
                return
    print("Book not found.")

def return_book():
    books = load_books()
    title = input("Enter the title of the book to return: ")
    for book in books:
        if book["title"].lower() == title.lower():
            if book["lent"] > 0:
                book["lent"] -= 1
                save_books(books)
                print(f'Book "{title}" returned successfully.')
                return
            else:
                print(f'No lent copies of "{title}" to return.')
                return
    print("Book not found.")
