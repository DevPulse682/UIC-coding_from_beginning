'''create a Circle class with a radius attribute and a method area() that returns the circles area'''


class Circle:
    def __init__ (self, radius):
        self.raduis = radius
        
    def area(self):
        return self.raduis ** 2 * 3.14
    
    def length(self):
        return 2 * 3.14 * self.raduis
        
        
c1 = Circle(
    radius=5

)

print(c1.length(),
      c1.area())