class Flyer:
    
    def move(self):
        print("flyer flies...")
        
    
class Swimmer:
    
    def move(self):
        print("Swimmer flies")
        

class Goose(Flyer, Swimmer):
    pass

g = Goose()
g.move()
print(Goose.mro())