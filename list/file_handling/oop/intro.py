class Phone:
    def __init__(self, name, year, price, color):
        self.name = name
        self.year = year
        self.price = price
        self.color = color

    def call(self):
        print("Calling.....")

    def play(self):
        print("Playing music.....")




shamsiddins_phone = Phone(
    name="Samsung Galaxy 22",
    year=2022,
    price=1200,
    color="Black"
)

samariddins_phone = Phone(
    name="Iphone 14",
    year=2022,
    price=1500,
    color="White")


shamsiddins_phone.call()
samariddins_phone.play()