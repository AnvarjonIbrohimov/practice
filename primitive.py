print("================ number =======================")
# in JAVA, vatiable is a name storage location
# in PYTHON, variable is a named reference to a value

counter = 100
print(counter)
counter = counter + 1 
print(counter)
counter += 1  
print(counter)
counter -= 1  
print(counter)
counter *= 2  
print(counter)
counter_type = type(counter)
print("counter type:", counter_type)
print(f"counter value: {counter}, counter type: {counter_type}")
result = counter.bit_count()
result2 = counter.numerator
print(result, result2)

print("================ string =======================")
# METHODS: upper(), lower(), title(), split(), join(), replace(), find()

course = "AI python fullstack"
result3 = type(course)
print(f"the type of course is: {result3}")
result4 = course.title()     # faqat bosh harflarini katta harfga aylantiradi
print(f"the title of the course is: {result4}")

result5 = course.lower()     # hamma harflarni kichik harfga aylantiradi
result6 = course.upper()     # hamma harflarni katta harfga aylantiradi 
print(f"the lower case of the course is: {result5}")
print(f"the upper case of the course is: {result6}")
result6 = course.replace("python", "java")  # string ichidagi so'zni boshqa so'zga almashtiradi
print(f"the replaced course is: {result6}")
result7 = course.split()    # stringni bo'sh joy bo'yicha bo'lib, ro'yxatga aylantiradi
print(f"the split course is: {result7}")

print("================ boolean =======================")
