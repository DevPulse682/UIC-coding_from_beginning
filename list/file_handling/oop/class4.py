'''
count how many pets created create a class method that tells how many pets instances have been made
'''

class Pet:
    cnt = 0
    
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Pet.cnt += 1

    @classmethod
    def count(cls):
        return cls.cnt
    
    
p1 = Pet("Dog", "Black")
p2 = Pet("Cat", "White")
p3 = Pet("Parrot", "Green")

print(Pet.count())