'''
    (1)  ENCAPSULATION => Himoyalash manosini bildiradi (JS => public, private, protected)  
    (2)  INHERITANCE => ameros degan manoda keladi parent class dan child classga property pass qilish (state, method) meros berish
    (3)  POLIMORPHISM => bir narsaning bir necha hil shakli
'''
print("============= INHERITANCE =============")

# Parent class


class Animal():    # () <= qoymasa xam boladi
    # state
    description = " The class creates animals"
    # constructor

    def __init__(self, voice):
        self.voice = voice
    # method

    def make_voice(self):
        print(f" The animal can make voice: {self.voice}")

# Child class


class Dog(Animal):     # (Animal) dan exstend boldi
    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)       # Parentga data yuborish
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def protect(self):
        print(" Yes, I can protect you!")

    def make_voice(self):
        print(f" The {self.name} can make voice: {self.sound}")


# Child class
class Cat(Animal):     # (Animal) dan exstend boldi
    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)       # Parentga data yuborish
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def protect(self):
        print(" Yes, I can protect you!")

# Child class


class Fish(Animal):     # (Animal) dan exstend boldi
    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)       # Parentga data yuborish
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def swin(self):
        print(" Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("===========================================")
dog.make_voice()
fish.make_voice()

print("============= POLIMORPHISM =============")
dog.make_voice()
fish.make_voice()

print("-----------------")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)    # fish =>  Fishdan olingan isntance mi?
b = isinstance(fish, Animal)   # fish => Animaldan olingan isntance mi?
c = isinstance(fish, object)    # fish =>  objectdam olingan isntance mi?
result = a and b and c
print(f"the result: {result}")


# Fish > Anima; > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data1:", data1, data2)
