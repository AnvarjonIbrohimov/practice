'''
CLASS
    (1) What is class?
    (2) ordinary vs static properties
    (3) special methods
'''

print("============================= What is class?  =================================")
# classlar obect yasab beruvchi shablon 
# class - blueprint 
# structure => state constructor method

class Person ():
    # static state property
    message = "class state property"

    # constructor 
    def __init__(self, name, age):  # self bu Person dan yaratilgan object hisoblanadi == js dagi (this)
        self.name = name   # this.name = name
        self.age = age      # this.age = age
    # method 
    def introduce(self):
        print(f" {self.name} says: How do you do!")

    def say_age(self):
        print(f" {self.name} says I am {self.age}!")

    @classmethod 
    def explain(cls):
        print("Class: static method property executed!")

person1 = Person("Jasica", 23)
person2 = Person("Jamshid", 27)
person3 = Person("Sattor", 21)

# ordinary state (oddiy state)
print(person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("=============================  static proporties  =================================")
# static property bu togridan togri class bilan keladigan state yoki method hisoblanadi
new_message = Person.message
print("new_message:", new_message)

# static method 
Person.explain()













