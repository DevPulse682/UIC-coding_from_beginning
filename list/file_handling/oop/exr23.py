class Shape:
    
    def area(self):
        raise NotImplementedError("not implemented")
    
    

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    
    def area(self):
        return self.width*self.height
    

class Circle(Shape):
    
    def __init__(self, r) -> None:
        self.r = r
        
    def area(self):
        import math 
        return math.pi*self.r**2
    
    

r = Rectangle(6,5)
c = Circle(4) 
v = Shape()

print(r.area())
print(c.area())

