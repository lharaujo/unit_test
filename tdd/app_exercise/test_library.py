import library

def test_add_book(): 
    lib = library.Library()
    book = library.Book("The Lord of the Rings", "J.R.R. Tolkien")
    lib.add_book(book.title, book.author)
    assert lib.list_books() == [(book.title, book.author)]

def test_remove_book():
    lib = library.Library()
    book = library.Book("The Lord of the Rings", "J.R.R. Tolkien")
    lib.add_book(book.title, book.author)
    lib.remove_book(book.title)
    assert lib.list_books() == []

def test_search_books_by_author():
    lib = library.Library()
    book1 = library.Book("The Lord of the Rings", "J.R.R. Tolkien")
    book2 = library.Book("Harry Potter", "J.K. Rowling")
    lib.add_book(book1.title, book1.author)
    lib.add_book(book2.title, book2.author)
    books = lib.search_books_by_author("J.R.R. Tolkien")
    assert books == [(book1.title, book1.author)]

def test_generate_statistics():
    lib = library.Library()
    book1 = library.Book("The Lord of the Rings", "J.R.R. Tolkien")
    book2 = library.Book("Harry Potter", "J.K. Rowling")
    lib.add_book(book1.title, book1.author)
    lib.add_book(book2.title, book2.author)
    stats = lib.generate_statistics()
    assert stats == {
        'total_books': 2,
        'unique_authors': {'J.R.R. Tolkien', 'J.K. Rowling'},
    }
