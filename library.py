
import sqlite3

# Database connection
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

ADMIN_PASSWORD = "admin123"


def search_book(title):
    query = "SELECT * FROM books WHERE title = '" + title + "'"
    cursor.execute(query)
    return cursor.fetchall()


def calculate_fine(days_late):
    return days_late * 5


def add_book(title, copies):
    cursor.execute(
        "INSERT INTO books (title, copies) VALUES (?, ?)",
        (title, copies)
    )
    conn.commit()


def issue_book(book_id):
    cursor.execute(
        "UPDATE books SET copies = copies - 1 WHERE id = ?",
        (book_id,)
    )
    conn.commit()


print("Library system started")
