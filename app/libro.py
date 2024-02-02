class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        
    def show_info(self):
        return f"Book {self.title} author: {self.author} year: {self.year} pages: {self.pages}"