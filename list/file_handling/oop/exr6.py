'''add a method intrduce() to Person that prints "Hi, i am ." and test it'''


class Person:
    def __init__ (self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I am {self.name}.") 
        


p1 = Person(
    name="John"
)

p1.introduce()