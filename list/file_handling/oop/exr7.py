'''write a class Rectangle that calculates and prints its area and perimeter using instance methods'''

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calc_perimeter(self):
        return (self.height + self.width) * 2
    
    def calc_area(self):
        return self.height * self.width
    
rect1 = Rectangle(
    height=5,
    width=7
)

print(rect1.calc_perimeter())
print(rect1.calc_area())

