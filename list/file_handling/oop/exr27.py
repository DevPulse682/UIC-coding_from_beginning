'''
create a class point with __add__ to support vector addition.

'''


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    
    def __add__(self, other):
        return Point(self.x +other.x, self.y + other.y)
    
    def __str__(self):
        return f"Point<{self.x}, {self.y}>"
        
        
        
p1 = Point(x=1, y=0)
p2 = Point(x=3, y=-1)
res=p1+p2
print(res)















