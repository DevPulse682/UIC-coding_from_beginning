class Car:
    cnt = 0
    
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color
        Car.cnt += 1
        
        
    def __str__(self):
        return self.name
    
    def __del__(self):
        Car.cnt -= 1
        del self

c1 = Car(
"BMW", 10000, "Black"
)
c2 = Car(
"Mercedes", 15000, "White")
c3 = Car(
"Toyota", 20000, "Red")

print(Car.cnt)

del c3

print(Car.cnt)