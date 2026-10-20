'''
combine isintstance() and duck typign: accept only objects that
have a specific method or belong to a specific base class
'''

class Base:

    def basemethod(self):
        raise NotImplementedError
    
    
class Child1(Base):
    
    def basemmethod(self):
        print("Child has base method")
        

class IndepClass:
    def basemethod(self):
        print("indepent class also hase basemethod")
        
        

def func(obj):
    if isinstance(obj, Base):
        obj.basemethod()
    else:
        print("basening yoki uning bolalarning mahsuloti emas!")
    
    
func(Child1())
func(IndepClass())