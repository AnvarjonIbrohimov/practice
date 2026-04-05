'''
Functions 
  (1) DEFINE vs CALL
  (2) ARGUMENTS vs PARAMETERS 
  (3) Keyword & default arguments
  (4) Scope: local vs global variable
'''

print("================ Define (parameters) vs Call (arguments) =======================")
# build in function: print(), type(), input(), bool(), int(), str()
# function malum bir vazifani bajaradigan kod blokidir.
# functionni yaratish uchun def kalit so'zidan foydalanamiz.  
# js da yoki Java da {} bilan kod blokini yaratamiz, 
# python da esa indentatsiya (4 ta bo'sh joy) bilan kod blokini yaratamiz.
# pass kalit so'zi functionni yaratish uchun ishlatiladi, lekin function ichida hech qanday kod yo'q.


# DEFINE: parameters > qismida biz def kalit so'zidan foydalanib, functionni yaratamiz. 
def greet(a):
    print( f"Hello, {a}! How are you?")


def greeting(name):
    print("greeting is executed ")
    return f"Hello, {name}!"

# CALL: arguments > qismida biz functionni chaqiramiz, ya'ni functionni ishlatamiz.
result1 = greet("Anvarjon")
print("result1:", result1)

result2 = greeting("Alex")
print("result2:", result2)

# Functionlar criteriya bo'yicha 2 ga bo'linadi void function va return function.
# void function > bu function hech qanday qiymat qaytarmaydi, ya'ni return
# return function > bu function qiymat qaytaradi, ya'ni return kalit so'zidan foydalanamiz.


print("================ Keyword & default arguments =======================")
# DEFINE
def give_greet(name, age=12):
    print("give_greet is executed")
    return f"Hello, {name}! You are {age} years old."


# CALL
# Keyword arguments > bu argumentsni functionga berishda, argumentning nomini ko'rsatib berish.
result3 = give_greet(name="Anvarjon", age=25) # Keywords arguments
result4 = give_greet("Elena")          # Keywordsiz
print("result3:", result3)
print("result4:", result4)

print("================ Scope: local vs global variable =======================")
# Scope > bu variablega qaysi qismda murojaat qilish mumkinligini belgilaydi.
# Local variable > bu variable function ichida yaratilgan va faqat function ichida mavjud bo'lgan variable.
# Global variable > bu variable function tashqarisida yaratilgan va butun kod bo'ylab mavjud bo'lgan variable.

b = 10 #3 global variable

# DEFINE
def calculate(a,b): #2 parameters
    c= a * b     #1 local variable
    print(f"the sum of {a} and {b} is: {c}")


# CALL
calculate(5, 10)