'''
    (1) What is an object? 
    (2) Iterable object & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''
import array   # package/module
from email import message
# bu pythonning standart kutubxonasi bo'lib, matematik funksiyalarni o'z ichiga oladi. Masalan, sqrt, ceil, floor, fabs va hokazo.
import math
# bu math modulidan faqat kerakli funksiyalarni import qilish imkonini beradi. Bu, odatda, kodni yanada o'qilishi va samarali qilish uchun ishlatiladi.
from math import sqrt, ceil, floor, fabs, asin
print("==================== What is an object? ====================")
# Object ozining state method propertylariga ega
# Pythonda hamma narsa obekt hisoblanadi. Masalan, int, str, list, dict va hokazo.

# Bular hammasi classlardan yaratilgan obektlardir. Har bir obekt o'zining classiga tegishli bo'lib, o'zining xususiyatlari va metodlariga ega.
print(type("Hello, World!"))  # <class 'str'>
print(type(42))               # <class 'int'>
print(type([1, 2, 3]))        # <class 'list'>
print(type(True))       # <class 'bool'>
print(type(array))      # <class 'module'>
print(type(math))       # <class 'module'>

print(sqrt(16))           # 4.0
print(ceil(3.7))          # 4
print(floor(3.7))         # 3
print(fabs(-5))           # 5
print(asin(1))            # 1.5707963267948966 (pi/2) bu
# #홀수 짝수 구별하기
# number = int(input("정수를 입력하시오: "))
# if ((number%2)==0):
#     print("입력된 정수는 짝수 입니다"  )
# else:
#     print("입력된 정수는 홀수 입니다")

# Programming paradingms
# OOP => Object Oriented Programming: bu dasturlash paradigmasi obektlarga asoslangan bo'lib, obektlar o'zining xususiyatlari va metodlariga ega. OOP da classlar yordamida obektlar yaratiladi va ular o'zaro aloqada bo'lishi mumkin.
# OOP 4: Encapsulation, Inheritance, Polymorphism, Abstraction
# Encapsulation => bu obektning xususiyatlari va metodlarini bir joyga to'plash va ularni tashqi dunyodan himoya qilish. Bu, odatda, classlar yordamida amalga oshiriladi.
# Inheritance => bu bir classning boshqa classdan xususiyatlari va metodlarini
# Polymorphism => bu bir nechta classning bir xil nomdagi metodlarini turli xil ishlatish imkonini beradi. Bu, odatda, method overriding yoki method overloading orqali amalga oshiriladi.
# Abstraction => bu murakkab tizimlarni soddalashtirish va ularni boshqarish uchun kerakli bo'lgan xususiyatlar va metodlarni ajratib ko'rsatish. Bu, odatda, abstract classlar yoki interface'lar yordamida amalga oshiriladi.
# FP => Functional Programming: bu chiziqli dasturlash paradigmasi bo'lib, funksiyalarni birinchi darajali obektlar sifatida ko'rib chiqadi. FP da funksiyalar o'zaro aloqada bo'lishi mumkin va ular o'zgaruvchan holatga ega emas.

print("==================== Error handling system ====================")
car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    a = car_dict.message["kukku"]
    print("passed here:")
    result = car_dict["year"]
    print("result: ", result)
# except (KeyError, AttributeError) as err:


except Exception as err:
    print("No origin data, General Error", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")
