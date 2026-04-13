print("===================== Iterable object & RANGE ====================")
# Iterable objects => string dict tuple list range map filter

text = "MIT"
for letter in text:
    print(letter)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):    # [ 0,5 )
    print(f"the elent {i}")

print("========================= DICTIONARY =======================")
# Dictionaryni JSON object xam deb ataladi 
# 👉 Dictionary — bu key-value (kalit–qiymat) ko‘rinishida ma’lumot saqlovchi data type
person_obj = dict(name="Jasur", age=15, single=True)  # kop holatlarda shu ishlatiladi
person = {"name": "Alex", "age": 20, "single": True}  
person_obj["phone"]="01012345678"
print("person_obj:", person_obj)
person_obj["email"] = "201946044@hs.ac.kr"

print("========================= DICTIONARY =======================")
print("person_obj:", person_obj)
print("person:", person)

name = person_obj["name"]
print("name:", name)

# method: get()
# name1 = person_obj["color"] bu yol bilan error hosil boladi
name1 = person_obj.get("color") # bunda esa error orniga None qiymat qaytaradi
print("name1:", name1)
hobby = person_obj.get("hobby", "Futbool")  # bundan shu qoymatni qoshib beradi
print("hobby:", hobby)

del person_obj["single"]   # bu shu key dagi datani delete qilib beradi
for key in person_obj:
    print(f"the key: {key} \nthe value: {person_obj[key]}")


