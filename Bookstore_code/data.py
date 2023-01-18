#different genres

genres = ['Romance', 'Action', 'Adventure', 'Horror', 'Comedy']

#Data Needed - genre, author_name, book_name, rating, publication_year, isbn

class book:
    def __init__(self, author_name, book_name, publication_year, genre, isbn, rating=0):
        self.author_name = author_name
        self.book_name = book_name
        self.publication_year = publication_year
        self.genre = genre
        self.isbn = isbn
        self.rating = rating
    
    def get_book(self):
        self.book = [self.author_name, self.book_name, self.publication_year, self.genre, self.isbn, self.rating]
        return self.book

class bookstore_data:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        return self.books.append(book.get_book())

    def remove_book(self, value):
        for book in self.books:

            if book[-2] == value[-2]:
                temp = self.books[-1]
                self.books[-1] = book
                self.books[self.books.index(book)] = temp             
                self.books.pop()

    def get_books(self):
        return self.books

















#testing

new_romance1 = book('Sarah J. Mass', 'A Court of Thorns and Roses', '2020', 'Romace', '1635575567', 4)
new_romance2 = book('Colleen Hoover','Ugly Love: A Novel', '2014', 'Romace', '1476753180', 2)
romance = bookstore_data()


romance.add_book(new_romance1)
romance.add_book(new_romance2)
print(romance.get_books())
romance.remove_book(new_romance1)


print(romance.get_books())





















#, ['Romance', ]