'''
    (1)  ENCAPSULATION => Himoyalash manosini bildiradi (JS => public, private, protected)  
    (2)  INHERITANCE => 
    (3)  POLIMORPHISM => 
'''

print("====================== ENCAPSULATION =========================")
'''
  PYTHON => public    =>    name    ( shunchaki nomni ozi kifoya )
            private   =>    __name  ( pasti ikta chiziqcha va name )
            protected =>    _name   ( pastki bitta chiziqcha va name )
'''

class Account ():
  # state
  description = "The class makes bank accounts"

  # constructor
  def __init__(self, owner, amount):
    self.__owner = owner
    self.__amount = amount
    pass

  # method
  def get_balance(self):
    print(f"the owner {self.__owner} has {self.__amount} usd")

  def kirim(self, amount):
    print("Kirim:", amount)
    self.__amount += amount 

  def chiqim(self, amount):
    print("Chiqim: ", amount)
    self.__amount -= amount

  @property   # Getter hisoblanadi property decorator orqali tashqaridan oqish imkonini beradi
  def holder(self):
    return self.__owner 
  
  @holder.setter  # __owner o'zgaruvchisini yangilash uchun yangi qiymat kiritish mumkin.
  def holder(self, new_owner):
    print("@holder.setter:", new_owner)

    self.__owner = new_owner
  
  def change_ownership(self, new_owner):
    print("change_ownership:", new_owner)
    self.__owner = new_owner

# ===========================================================

my_account = Account("Shawn", 1000)
my_account.get_balance()

print('---------------')
my_account.kirim(3500)
my_account.chiqim(400)
my_account.get_balance()

# print(my_account.owner)  error chiqadi

try:
  result = my_account.__amount  # error chiqarish uchun qildik, aslida bu private bolgani uchun tashqaridan togrida togri chaqira olmaymiz
  print("result:", result)
except Exception as err:
  print("Bunday state topilmadi: ", err)

account_owner = my_account.holder  # state singari ishlatyabmiz
print("account_owner:", account_owner)

# my_account.change_ownership("Alex")
my_account.holder = "Alex"  # bu (holder) setter methodini chaqiradi va __owner ozgaruvchini yangilab beradi

print("account_owner:", my_account.holder)
