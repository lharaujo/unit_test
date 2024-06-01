"""For this exercise, you'll need to create a library object comprising 5 methods: 
    - addbook, which will take the title and author as parameters. 
    - deletebook which will take the title of a book as parameter (deletion only possible on the title). 
    - listbook** returns a list of books currently added. 
    - searchbookauthor** will return books by author only. 
    - generationstat** returns the number of books and a set of unique authors.
    """


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library(Book):
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def list_books(self):
        return [(book.title, book.author) for book in self.books]

    def search_books_by_author(self, author):
        return [(book.title, book.author) for book in self.books if book.author == author]

    def generate_statistics(self):
        total_books = len(self.books)
        unique_authors = set(book.author for book in self.books)
        return {
            'total_books': total_books,
            'unique_authors': unique_authors,
        }

lib = Library()
book = Book("The Lord of the Rings", "J.R.R. Tolkien")
print(book)