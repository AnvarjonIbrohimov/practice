'''
CLASS
    (1) What is class?
    (2) ordinary vs static properties
    (3) special/magic methods
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

print("============================= special methods  =================================")
# special/magic methodlarni "python magic method rszalski > https://rszalski.github.io/magicmethods/" shu yerda korsak boladi 
# __init__  __new__ __str__ __call__ __getitem__ __eq__ __len__ ...
class Car():
    # state
    description = "This class makes car"

    
    def __new__(cls, *args):  # bu yangi object yasayabdi  (cls) bu classning ozini anglatadi
        print("*__new__")
        return super().__new__(cls)  # bu yuqoridagi class dan object yaratish uchun 
    
    def __init__(self, name, year): 
        self.name = name
        self.year = year

    #method
    def start_engine(self):  
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"

    def __call__(self):
      print(f"Object called as function!")
      return True

my_car = Car("tOYOTA", 2024)
my_car.start_engine()
my_car.stop_engine()

print("-----------------")
your_car = Car("Ferrari", 2025)
print(your_car)
response = your_car()  # call
print("response: ", response)


