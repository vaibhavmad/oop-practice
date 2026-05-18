class Members:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.available: 
            print(f"{self.name} borrowed {book.title}.")
            book.available = False
            self.borrowed_books.append(book.title)
        else:
            print(f"{book.title} is not available.")
        
    def return_book(self, book):
        if book.title in self.borrowed_books:    
            print(f"{self.name} returned {book.title}.")
            book.available = True
            self.borrowed_books.remove(book.title)
        else:
            print(f"{book.title} is not with {self.name}.")
            
    def borrowed_books_list(self):
        if self.borrowed_books:
            print(f"{self.name} currently has the following books")
            for index, book in enumerate(self.borrowed_books):
                print(f"{index + 1}. {book}")
        else:
            print(f"Currently no book has been borrowed by {self.name}")