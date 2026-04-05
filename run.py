print("*"*35)
a = 100
print(a + 1)
name = "Anvarjon"
message = "Hello"
print("message", type(message))
print(message + f" {name}! How are you?")
print("*"*35)
# Dunder __buildins__, __init__
print(dir(__builtins__))
print("*"*35)
def my_func():
    print("This is my function")
    return "Hello from my function"
result = my_func()
print(result)
print("*"*35)
def add_numbers(x, y):
    return x + y  
result = add_numbers(5, 10)
print(result)
print("*"*35)
def greet(name):
    return f"Hello, {name}!"
greeting = greet("Anvarjon")
print(greeting)
print("*"*35)


i = 2
for i in range(5):
    print(i)

