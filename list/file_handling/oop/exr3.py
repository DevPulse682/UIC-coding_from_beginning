'''define a book class and create three different book objects representing different titles'''


class Book:
    def __init__(self, title):
        self.title = title
        
        
        
book1 = Book(
    title="The Great Gatsby")


book2 = Book(
    title="To Kill a Mockingbird")

book3 = Book(
    title="Box")


print(f"Book 1: {book1.title}")
print(f"Book 2: {book2.title}")
print(f"Book 3: {book3.title}")