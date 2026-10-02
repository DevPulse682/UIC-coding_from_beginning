'''create a dog class with a method bark() that prints "Woof!" when called call it from an object'''


class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def bark(self):
        print("Woo000000000f!")
        
        
d1 = Dog(
    name="REks",
    age=3,
    color="brown"
)
d1.bark()