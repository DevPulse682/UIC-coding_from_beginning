class Cat:
    def __init__(self, name):
        self.name = name
        

class Dog:
    def __init__(self, name):
        self.name = name
        
        
c1 = Cat("Tom")
d1 = Dog("Jerry")

print(isinstance(c1, Dog), isinstance(d1, Dog))

