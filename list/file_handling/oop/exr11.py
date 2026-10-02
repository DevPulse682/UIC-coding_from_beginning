'''write a BankAccount class with methods deposit() and withdraw() modifying an instance variable balance'''


class BankAccount:
    called_count = 0
    
    def __init__(self, balance, name, card_number):
        self.balance = balance
        self.name = name
        self.card_number = card_number

    def deposit(self, amount: int):
        self.balance = self.balance + amount
        
        
    def withdraw(self, amount: int):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance = self.balance - amount
        
    
    


shamsiddins_card = BankAccount(
    balance=100000,
    name="Shamsiddin",
    card_number="1234-5678-9012-3456"
)

shamsiddins_card.withdraw(30000)
print(shamsiddins_card.balance)

shamsiddins_card.deposit(100000)
print(shamsiddins_card.balance)

shamsiddins_card.withdraw(150000)
print(shamsiddins_card.balance)


        