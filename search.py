from file_handler import load_books

def search_book():
    books = load_books()
    title = input("Enter the title of the book to search for: ")
    for book in books:
        if book["title"].lower() == title.lower():
            print(f"Book found: {book['title']} by {book['author']} (ISBN: {book['isbn']}), "
                  f"Published in {book['year']}, Price: ${book['price']}, "
                  f"Stock: {book['quantity']}, Lent: {book['lent']}")
            return
    print("Book not found.")
