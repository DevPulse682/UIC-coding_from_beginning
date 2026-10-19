'''
Polymorfizm ota klassdigi attributlarni ishlatmasdan ozimiz implementatsiya qilishimiz kerak
Kod takrorlanishining oldini oladi: Bir xil vazifani bajaruvchi turli obyektlar uchun alohida funksiyalar yozish shart emas.

Kengaytiruvchanlik (Extensibility): Yangi sinf qo'shish dasturning qolgan qismlarini o'zgartirmasdan turib amalga oshiriladi (faqat o'sha metodni yangi sinfda yozish kifoya).

Moslashuvchanlik: Dasturni o'qish va tushunish osonlasha


'''


class Vehicle:
    
    def move(self):
        raise NotImplementedError("Method not implemented")
    
    
    

class Car(Vehicle):
    
    
    def move(self):
        print("vmm.........")
        
        

class Train(Vehicle):
    
    def move(self):
        print("puuvv.....")
        

c1 = Car()
t = Train()
v = Vehicle()

c1.move()
t.move()
