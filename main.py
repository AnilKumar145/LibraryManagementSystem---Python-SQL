from database import create_tables, add_book, issue_book, return_book, view_books

def menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View Available Books")
    print("5. Exit")

if __name__ == "__main__":
    create_tables()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)

        elif choice == '2':
            book_id = int(input("Enter book ID to issue: "))
            borrower_name = input("Enter borrower's name: ")
            issue_book(book_id, borrower_name)

        elif choice == '3':
            book_id = int(input("Enter book ID to return: "))
            return_book(book_id)

        elif choice == '4':
            view_books()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")
