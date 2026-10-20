class Animal:
    
    def live(self):
        print("Animal is living....")


class Flyer(Animal):
    
    def move(self):
        print("flyer flies...")
        
    
class Swimmer(Animal):
    
    def move(self):
        print("Swimmer flies")
        

class Goose(Flyer, Swimmer):
    pass

g = Flyer()
g.move()

print([cls.__name__ for cls in Flyer.mro()])