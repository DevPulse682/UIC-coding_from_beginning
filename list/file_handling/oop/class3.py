'''
make a class method that create a student from name, grade string like Anna 95
'''

class Student:
    def __init__(self, name, age):
        self.name  = name
        self.age = age
    
    @classmethod
    def create(cls, s: str):
        name, age = s.split(",")
        
        
        return Student(name=name, age=int(age))
    
        
    def __str__(self):
        return f"Student<{self.name}, {self.age}>"
    
    
st1 = Student("Shamsiddin", 22)
st2 = Student.create("Anna, 95")

print(st1, st2)

        