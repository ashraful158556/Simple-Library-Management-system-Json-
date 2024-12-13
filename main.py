import book_manager
import search
import lent_return

def main():
    while True:
        print("\nLibrary Management System")
        print("0. Exit")
        print("1. Add books")
        print("2. View all books")
        print("3. Update a book")
        print("4. Remove a book")
        print("5. Search for a book")
        print("6. Lend a book")
        print("7. Return a book")
        
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Exiting the system. Goodbye!")
            break
        elif choice == "1":
            book_manager.add_book()
        elif choice == "2":
            book_manager.view_books()
        elif choice == "3":
            book_manager.update_book()
        elif choice == "4":
            book_manager.remove_book()
        elif choice == "5":
            search.search_book()
        elif choice == "6":
            lent_return.lend_book()
        elif choice == "7":
            lent_return.return_book()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
