class Student:
    school = "ABC School"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        


st1 = Student("Shamsiddin", 22)
st2 = Student("Samariddin", 22)
print(st1.school, st2.school)