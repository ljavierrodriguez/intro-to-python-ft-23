from libro import Book

class Library:    
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def addBook(self, book: Book):
        self.books.append(book)
        
    def listBooks(self):
        print(self.name)
        print("===============================================")
        for book in self.books:
            print("-->", book.show_info())