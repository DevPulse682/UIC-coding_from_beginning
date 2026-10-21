class Player:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__ (self):
        return f"Player<{self.name}, {self.age}>"
        
        
class Team:
    
    def __init__ (self, name: str, memebers: list[Player]):
        self.__name = name
        self.__members = members
        
    def add_player(self, name, age):
        new_player = Player(name=name, age=age)
        self.__members.append(new_player)
        return True
        
    def __str__ (self):
        return f"Team<{self.name}>"