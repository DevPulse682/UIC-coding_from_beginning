class Logger:
    
    def __init__(self, max_lines: int) -> None:
        self.max_lines = max_lines
        
    def log(self, msg: str) -> None:
        print(f"[LOG] {msg}")
        
        
        
class Saver:
    
    def __init__(self, is_db) -> None:
        self.is_db =is_db
    
    def save(self):
        print("Data saved")
        
        
class MyApp(Logger, Saver):
    
    def __init__(self, max_lines):
        Logger(max_lines = max_lines)
    
    
    def use(self):
        print("using my app.")
        


app1 = MyApp(
    max_lines=10
    
) 


app1.log("Salom")
app1.save()
app1.use()
print(app1.max_lines)
print(vars(app1))
print(MyApp.__mro__)