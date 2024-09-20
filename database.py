import sqlite3

def connect():
    return sqlite3.connect("library.db")

def create_tables():
    conn = connect()
    cur = conn.cursor()

    # Create the books table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        available INTEGER DEFAULT 1
    )
    """)

    # Create the issued_books table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS issued_books (
        book_id INTEGER,
        borrower_name TEXT NOT NULL,
        issue_date TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(book_id) REFERENCES books(id)
    )
    """)
    
    conn.commit()
    conn.close()

def add_book(title, author):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()
    print(f'Book "{title}" by {author} added to the library.')

def issue_book(book_id, borrower_name):
    conn = connect()
    cur = conn.cursor()

    # Check if the book is available
    cur.execute("SELECT available FROM books WHERE id = ?", (book_id,))
    result = cur.fetchone()

    if result:
        if result[0] == 1:  # Book is available
            cur.execute("INSERT INTO issued_books (book_id, borrower_name) VALUES (?, ?)", (book_id, borrower_name))
            cur.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
            conn.commit()
            print(f'Book ID {book_id} issued to {borrower_name}.')
        else:
            print("Book is already issued.")
    else:
        print("Book does not exist.")

    conn.close()

def return_book(book_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT book_id FROM issued_books WHERE book_id = ?", (book_id,))
    result = cur.fetchone()

    if result:
        cur.execute("DELETE FROM issued_books WHERE book_id = ?", (book_id,))
        cur.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
        conn.commit()
        print(f'Book ID {book_id} has been returned.')
    else:
        print("This book was not issued.")

    conn.close()

def view_books():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE available = 1")
    rows = cur.fetchall()

    if rows:
        print("\nAvailable Books:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")
    else:
        print("No books available.")

    conn.close()
