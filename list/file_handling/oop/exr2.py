'''Create a Person class with name and age attributes.
print formatted output using f-strings
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
person1 = Person(
    name="Shamsiddin",
    age=22)

print(f"Name: {person1.name}, Age: {person1.age}")