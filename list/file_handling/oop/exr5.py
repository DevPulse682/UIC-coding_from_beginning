'''define a student class where __init__ prints Now student created. when a new object is created'''

class Student:
    
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        
        print("Now student created.")

    def __del__(self):
        print("Student deleted.")
    
        
        
        
st1 = Student(
    name="John",
    age=20,
    id="o019-22"
)

del st1


