class Vehicle:
    def __init__(self, name, brand, color) -> None:
        self.name = name
        self.brand = brand
        self.color = color
        
        
    def move(self):
        print("Vehicle moving.....")
        
        
class Car(Vehicle):
    
    def move(self):
        print("g'nnnnnnnnnnnnnnnnn")
        
        

class Plane(Vehicle):
    
    def move(self):
        print("vzzzzzzzzzzz")
        
        
class Aircraft(Plane):
    def __init__(self, name, brand, color, weapon_capacity, target_accuracy) -> None:
        self.weapon_capacity = weapon_capacity
        self.target_accuracy = target_accuracy
        super().__init__(name, brand, color)
        
    def bomb(self):
        print("Bombing.....")

class PassengerCraft(Plane):
    def __init__(self, name, brand, color, passenger_capacity, first_class) -> None:
        self.passenger_capacity = passenger_capacity
        self.first_class = first_class
        super().__init__(name, brand, color)
        
    def take_off(self):
        print("taking off....")
        



plane = PassengerCraft(
    name = "Boeing 717",
    brand ="2121",
    color = "black",
    passenger_capacity= 1000,
    first_class= 500
)

plane.take_off()

