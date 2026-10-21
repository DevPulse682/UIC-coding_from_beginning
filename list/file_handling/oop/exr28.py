class Book:
    
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        
        
    
    def __eq__(self, other):
        is_equal = (self.title == other.tittle) and (self.author == other.author)
        return is_equal
        
    def __str__(self) -> str:
        return f"Book<tile={self.title}>"
    
    

b1 = Book(
    "Molxona",
    "Jorj oruell"
)

b2 = Book(
    "Start with why",
    "Simon Sinek"
)

print(b1 == b2)