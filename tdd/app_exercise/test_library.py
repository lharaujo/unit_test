import library

def test_add_book(): 
    lib = library.Library()
    lib.add_book("The Lord of the Rings", "J.R.R. Tolkien")
    assert lib.list_books() == [("The Lord of the Rings", "J.R.R. Tolkien")]

def test_remove_book():
    lib = library.Library()
    lib.add_book("The Lord of the Rings", "J.R.R. Tolkien")
    lib.remove_book("The Lord of the Rings")
    assert lib.list_books() == []

def test_search_books_by_author():
    lib = library.Library()
    lib.add_book("The Lord of the Rings", "J.R.R. Tolkien")
    lib.add_book("Harry Potter", "J.K. Rowling")
    books = lib.search_books_by_author("J.R.R. Tolkien")
    assert books == [("The Lord of the Rings", "J.R.R. Tolkien")]

def test_generate_statistics():
    lib = library.Library()
    lib.add_book("The Lord of the Rings", "J.R.R. Tolkien")
    lib.add_book("Harry Potter", "J.K. Rowling")
    stats = lib.generate_statistics()
    assert stats == {
        'total_books': 2,
        'unique_authors': {'J.R.R. Tolkien', 'J.K. Rowling'},
    }
