'''Define a car class with attributes 'brand' and 'model'. Create two objects and print their attributes.'''


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def driving(self):
        print("G'nnnn, G'nnnn, G'nnnn..... tutututututu..... 🛞🔊🚙")


car1 = Car(
    brand="BMW",
    model="X5"
)

car1.driving()
