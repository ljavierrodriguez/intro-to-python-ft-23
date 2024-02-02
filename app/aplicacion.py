from biblioteca import Library
from libro import Book


book1 = Book("El asesinato en el oriente express", "Agatha Christie", "1926", 800)
book2 = Book("Los cuatro grandes", "Agatha Christie", "1926", 600)
book3 = Book("Un crimen dormido", "Agatha Christie", "1976", 1200)


library = Library("Biblioteca de Alexandria")
library.addBook(book1)
library.addBook(book2)
library.addBook(book3)


library.listBooks()