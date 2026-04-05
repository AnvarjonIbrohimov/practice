***********************************************************
Pythonda hamma narsa object hisolanadi

Dunder   # bu ikki __ pastki chiziqsa hisoblanadi
👉 "dunder" = double underscore (__)
👉 Python ichki (maxsus) metodlari
👉 Odatda object (class) bilan ishlaydi
***********************************************************

__init__
👉 Class yaratilganda avtomatik ishlaydi
👉 constructor (boshlang‘ich sozlash)
  class User:
    def __init__(self, name):
        self.name = name
***********************************************************
🔹 __builtins__
  👉 Python ichida default bor narsalar
  👉 masalan: print(), len()
  👉 ya’ni tayyor funksiyalar to‘plami

***********************************************************
In pyhthon, there are builtin tools:
1. TYPES > int float str list dict:
  🔹 TYPES (ma’lumot turlari)
    int → butun son (5, 10)
    float → o‘nlik son (3.14)
    str → matn ("hello")
    list → ro‘yxat [1,2,3]
    dict → lug‘at {"a":1}

2. FUNCTIONS > print() len() input() type()
  🔹 FUNCTIONS:
    print() → ekranga chiqaradi
    len() → uzunligini hisoblaydi
    input() → foydalanuvchidan ma’lumot oladi
    type() → turini aniqlaydi
3. CONSTANS > True False None
     🔹 CONSTANTS
        True → rost
        False → yolg‘on
        None → hech narsa yo‘q (bo‘sh qiymat)
***********************************************************

# in JAVA, vatiable is a name storage location 
# in PYTHON, variable is a named reference to a value

# result = counter.bit_count() 
      👉 Kasr = 3 / 4 
          3 → yuqorisi (numerator)
          4 → pastki qismi (denominator)
# result2 = counter.numerator

.isnumeric()    👉 string ichida faqat raqam bormi tekshiradi
                  "123".isnumeric() → True
                  "12a".isnumeric() → False
                  
***********************************************************