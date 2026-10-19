'''
Inkapsulyatsiya (Encapsulation) — bu Obyektga yo'naltirilgan dasturlashning (O'YD) asosiy 4 ta tamoyilidan biri bo'lib,
ma'lumotlarni (o'zgaruvchilarni) va ular bilan ishlaydigan funksiyalarni 
(metodlarni) yagona sinf (class) ichida birlashtirish hamda tashqi muhitdan himoya qilish jarayonidir.

. Bitta tag chiziq: _protected (Himoyalangan)
Ma'nosi: Bu dasturchilar o'rtasidagi kelishuv (konvensiya) hisoblanadi.
U "Bu atribut yoki metod ichki foydalanish uchun mo'ljallangan,
uni sinf tashqarisidan to'g'ridan-to me'yorida ishlatmang" degan ogohlantirish beradi.

2. Ikkita tag chiziq: __private (Maxfiy / Yopiq)
Ma'nosi: Bu Python tilining o'zi tomonidan qat'iy himoya qilinadigan va yashiriladigan atribut/metoddir.

Kirish: Sinf tashqarisidan to'g'ridan-to'g me'yorida murojaat qilib bo'lmaydi. Aks holda AttributeError xatoligi beradi.

Ishlash mexanizmi (Name Mangling): Python __variable nomini avtomatik ravishda _ClassName__
variable ko'rinishiga o'zgartirib qo'yadi.
Bu orqali voris (child) sinflarda bir xil nomli atributlar bir-biri bilan to'qnashib ketishining oldi olinadi.

'''


class Person:
    def __init__(self, name, age, passport, jshshir) -> None:
        self.name = name
        self.age = age
        self.__passport = passport
        self.__jshshir = jshshir
        
        
    def change_passport(self, new_passport):
        self.__passport = new_passport    
    
    
p1 = Person(
    "eshmat", 19, "AA12345", "42332543646"
)

p1.name = "Toshmat"
p1.__passport = "eshmatni passporti"


print(p1.name, p1.age)
print(vars(p1))