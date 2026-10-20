from typing import Any

class One:
    
    def run(self):
        print("one is running...")
        
        
class Two:
    
    def run(self):
        print("two is running")
        
class Three:
    
    def walk(self):
        print('Walking....')            
    
    
def start(obj: Any):
    obj.run()
    
    
one1 = One()
two1 = Two()
#three1 = Three()


start(one1)
start(two1)
#start(three1)