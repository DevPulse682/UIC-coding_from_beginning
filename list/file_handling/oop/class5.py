'''
make default book create a class method that makes a book with title unknown and author unknown

'''


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author  = author
        
    @classmethod
    def default_book(cls):
        return cls(title="Unknown", author="Unknown")
    

b1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
b2 = Book.default_book()

print(b1.title, b1.author)
print(b2.title, b2.author)
    
