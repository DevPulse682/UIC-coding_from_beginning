class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    
    @classmethod
    def from_diameter(cls, diameter):
        return Circle(radius=diameter/2)
    
    def __repr__(self):
        return f"Circle<r={self.radius}>"
    

c1 = Circle.from_diameter(10)

print(c1)