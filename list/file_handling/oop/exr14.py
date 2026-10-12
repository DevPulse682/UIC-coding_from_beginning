class Animal:
    
    
    def __init__(self, name, color):
        self.name = name
        self.color = name

class Cat(Animal):
    
    
    def play(self):
        print("Meooow")



class Dog(Animal):
    
    
    
    def play(self):
        print("Wooof....")
        


d1 = Dog(
    name="Reks",
    color="Black"
    
)


c1 = Cat(
    name="mosh",
    color="jiggarang"
)

c1.play()
d1.play()
