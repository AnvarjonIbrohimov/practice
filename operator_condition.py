''' OPERATOR & CONDITIONs
  (1) Operator
  (2) Condition
  (3) Logical Operator
'''

print("========= Operator =========")
# + - > >= < <= * /   // % += **

# Arithmetic(matematik) operatorlar
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a // b)  # 3 (butun bo‘lish)
print(a % b)   # 1 (qoldiq)
print(a ** b)  # 1000 (daraja)

# Comparison (solishtirish) operatorlar
c = 5
d = 10
print(c == d)  # False
print(c != d)  # True
print(c > d)   # False
print(c < d)   # True
print(c >= d)  # False
print(c <= d)  # True

# Logical (mantiqiy) operatorlar
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Assignment (o‘zlashtirish)
x = 5
x += 3   # x = x + 3 → 8
x -= 2   # 6
x *= 2   # 12

aa = dict(name="Alex", age=30)
bb = dict(name="Alex", age=30)
cc = aa
print("aa==bb", aa == bb)  # only value checking
print(id(aa), id(bb))
print("cc is aa: ", cc is aa)

aaa = [1, 2, 3]
bbb = [1, 2, 3]

print(aaa == bbb)  # True (qiymati bir xil)
print(aaa is bbb)  # False (xotirada boshqa obyekt)

nums = [1, 2, 3]
print("nums:", nums)
print("2 in nums: ", 2 in nums)  # True

print("========= Condition =========")

age = 20
if age >= 18:
    print("Kirish mumkin")

age2 = 16
if age2 >= 18:
    print("Kirish mumkin")
else:
    print("Kirish mumkin emas")

score = 80
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")

age3 = 20
has_id = True
if age3 >= 18 and has_id:
    print("Kirish mumkin!")

person = "adult" if age3 > 18 else "minor"
print("person: ", person)

