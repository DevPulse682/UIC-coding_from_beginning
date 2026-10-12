class Phone:
    
    def __init__(self, name, price, color, brand):
        self.name = name
        self.price = price
        self.color = color
        self.brand = brand
        
        
    def call(self):
        print("Calling.....")
        
    
        
class Sotkaold(Phone):
    
    def __init__(self, name, price, color, brand, fonar):
        self.fonar = fonar
        super().__init__(name, price, color, brand)

    def play(self):
        print("Playing snake .....")
        
    def sms(self):
        print("Sending sms.....")


class Sotkanew(Phone):
    
    def __init__(self, name, price, color, brand, is_touchscreen):
        self.is_touchscreen = is_touchscreen
        super().__init__(name, price, color, brand)
    
    def play(self):
        print("Playing a diamond rush.....")
        
    def message(self):
        print("Sending message or internet message.....")

    def take_photo(self):
        print("Taking photo.....")
        
    def listen_music(self):
        print("Listening music.....")

class Smartphone(Phone):
    def __init__(self, name, price, color, brand, has_5g):
        self.has_5g = has_5g
        super().__init__(name, price, color, brand)

    def play(self):
            print("Playing a Efootball.....")
            
    def surfing_social_media(self):
            print("Surfing social media.....")
    
    def take_photo(self):
            print("Taking photo.....")
            
    def listen_music(self):
            print("Listening music.....")
            
    def using_ai(self):
            print("Hello AI.....")
        
        
        

class Tablet(Phone):
    
    def __init__(self, name, price, color, brand, has_stylus):
        self.has_stylus = has_stylus
        super().__init__(name, price, color, brand)
    
    def play(self):
                print("Playing a Efootball.....")
                
    def surfing_social_media(self):
                print("Surfing social media.....")
        
    def take_photo(self):
                print("Taking photo.....")
                
    def listen_music(self):
                print("Listening music.....")
                
    def using_ai(self):
                print("Hello AI.....")
            
    def write_on_tablet(self):
                print("Writing on tablet.....")
                
    

class Domashniy(Phone):
    
    def __init__(self, name, price, color, brand, is_wired):
        self.is_wired = is_wired
        super().__init__(name, price, color, brand)
    
    def call(self):
        print("Tooot Toot.....")



panasonic = Domashniy(
    name="P3454",
    price=50,
    color="White",
    brand="Panasonic",
    is_wired=True)

panasonic.call()

nokia3600 = Sotkaold(
    name="Nokia 3600",
    price=100,
    color="Black",
    brand="Nokia",
    fonar=True
)

nokia3600.call()

nokia1202 = Sotkanew(
    name="Nokia 1202",
    price=150,
    color="Black",
    brand="Nokia",
    is_touchscreen=False
)

nokia1202.listen_music()

Xiaomi = Smartphone(
    name="Xiaomi 12",
    price=1000,
    color="Black",
    brand="Xiaomi",
    has_5g=True
)

Xiaomi.using_ai()


ipad = Tablet(
    name="Ipad",
    price=1111,
    color="White",
    brand="Apple",
    has_stylus=True
)

ipad.write_on_tablet


print("Result --->", issubclass(Tablet, Phone))