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