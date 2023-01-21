#from heapq import heappop, heappush, heapify


#different genres

genres = ['Romance', 'Action', 'Adventure', 'Horror', 'Comedy']

#Data Needed - genre, author_name, book_name, rating, publication_year, isbn

class Book:
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

class Library:
    def __init__(self):
        self.library = []
        self.dict = {}
        self.inventory_dict = {}        
        
        self.total_book_count = 0

    def add_book_to_library(self,new_book):
        book_isbn = new_book.get_book()[-2]
        self.indiv_book_count = 1
        
         
        if book_isbn in self.dict.keys():
            #adding 1 to current books inventory if already in library
            self.inventory_dict[book_isbn] = (self.inventory_dict.get(book_isbn, self.indiv_book_count) + 1)
            return
            
        
        else:
            #setting up inventory dict
            self.inventory_dict[book_isbn] = self.indiv_book_count
            self.indiv_book_count += 1
            
            #adding book to library list
            self.library.append(new_book.get_book())
            
            # setting up new key/values for dict using the book isbn as keys and index of book in shelf as values
            self.dict[book_isbn] = len(self.dict)
            return
         
    def remove_book(self, book):
        
        book_isbn = book.get_book()[-2]
        
        if book_isbn not in self.dict:
            return

        if self.inventory_dict.get(book_isbn) > 1:
            #updating inventory
            self.inventory_dict.update({book_isbn:(self.inventory_dict.get(book_isbn))-1})

            return
            
        if self.inventory_dict[book_isbn] == 1:
                
            #swap list elements to keep dict integrity
            book_index = self.dict[book_isbn]
            swapped_book = self.library[-1][-2]
            self.library[-1], self.library[book_index] = self.library[book_index], self.library[-1]
           
            #change value of swapped element in dict
            self.dict[swapped_book] = book_index
            
            #removing book from library and dict
            del self.dict[book_isbn]
            self.library.pop()
            #updating inventory
            self.inventory_dict.update({book_isbn:0})
            return

    def get_library(self):
        return self.library

    def get_dict(self):
        return self.dict
    
    def get_inventory_dict(self):
        return self.inventory_dict
    
    def get_total_book_count(self):
        return sum(self.inventory_dict.values())

class sorter:
    def __init__(self, library):
        self.library = library
        self.shelf = []
        self.dict = {}


    def shelf_by_genre(self, genre):
        for book in self.library.get_library():
            if book in self.shelf:
                    continue 
            
            if genre == book[-3]:
                self.shelf.append(book)
        return self.shelf
    
    def rating_desc_by_genre(self):
        return sorted(self.shelf, key=lambda x:x[2], reverse=True)
        
    
    def get_shelf(self):
        return self.shelf
    

     
    
    
















#testing

new_book1 = Book('Sarah J. Mass', 'A Court of Thorns and Roses', '2020', 'Romance', 1635575567, 4)
new_book2 = Book('Colleen Hoover','Ugly Love: A Novel', '2014', 'Romance', 1476753180, 2)
new_book3 = Book('Hi', 'IDK', '2023', 'Romance', 9876543215, 5)
new_book4 = Book('Hi', 'IDK', '2023', 'Romance', 9876543215, 5)
new_book5 = Book('Sarah J. Mass', 'A Court of Thorns and Roses', '2020', 'Romance', 1635575567, 4)
new_book6 = Book('dan', 'martial', '2019', 'Action', 1234567895, 1)
library = Library()


library.add_book_to_library(new_book1)
library.add_book_to_library(new_book2)
library.add_book_to_library(new_book3)
library.add_book_to_library(new_book4)
library.add_book_to_library(new_book5)
library.add_book_to_library(new_book6)

print('\nfull library')
print(library.get_library())

print('\nfull dict')
print(library.get_dict())

print('\ninventory dict')
print(library.get_inventory_dict())

print('\nTotal book inventory')
print(library.get_total_book_count())

new_sort = sorter(library)

print('\nlist before sort before removal')
print(new_sort.shelf_by_genre('Romance'))

print('\nsorted list before removal')
print(new_sort.rating_desc_by_genre())

print('\nremoving book')
library.remove_book(new_book2)

new_sort2 = sorter(library)

print('\n')
print(library.get_total_book_count())

print('\n')
print(library.get_inventory_dict())

print('\nnew shelf')
print(new_sort2.shelf_by_genre('Romance'))

print('\nnew sorted list')
print(new_sort2.rating_desc_by_genre())

print('\n')
print(library.get_library())

print('\n')
print(library.get_dict())




















