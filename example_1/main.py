from books import Books
from members import Members

book_1 = Books("Atomic Habits", "James Clear")
book_2 = Books("Deep Work", "Cal Newport")

member_1 = Members("Vaibhav")
member_2 = Members("Rahul")

member_1.borrow_book(book_1)
print(member_1.borrowed_books)

member_1.borrow_book(book_2)
print(member_1.borrowed_books)

member_2.borrow_book(book_1)

member_1.return_book(book_2)
print(member_1.borrowed_books)

member_2.borrow_book(book_2)
print(member_2.borrowed_books)

member_1.borrowed_books_list()
member_2.borrowed_books_list()

book_1.check_availability()