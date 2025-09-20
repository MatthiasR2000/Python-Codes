

print("Basics of Python\n")
#Variable declarations and data types Note: Datatyopes in Python are dynamic and do not require explicit declaration.
number = 10
pi = 3.14
largeNumber = 1234567890.123456
text = "Hello, Python!"
isActive = True
complexNum = 2 + 3j

print(type(number))
print(type(pi))
print(type(largeNumber))
print(type(text))
print(type(isActive))
print(type(complexNum))

#Basic operations
sumResult = number + pi
print("Sum:", sumResult)
concatText = text + " Let's learn Python."
print(concatText)
isActive = not isActive
print("Is Active:", isActive)
magnitude = abs(complexNum)
print("Magnitude of complex number:", magnitude)
#String manipulations
upperText = text.upper()
print("Uppercase Text:", upperText)
substring = text[7:13]
print("Substring:", substring)
replacedText = text.replace("Python", "World")
print("Replaced Text:", replacedText)
splitText = text.split(", ")
print("Split Text:", splitText)
#List operations
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print("Fruits List:", fruits)
firstFruit = fruits[0]
print("First Fruit:", firstFruit)
fruits.remove("banana")
print("Fruits after removal:", fruits)
fruits.sort()
print("Sorted Fruits:", fruits)
#Dictionary operations
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Person Dictionary:", person)
person["age"] = 31
print("Updated Age:", person["age"])
person["profession"] = "Engineer"
print("Added Profession:", person)
del person["city"]
print("After Deleting City:", person)
keys = person.keys()
print("Keys:", list(keys))
values = person.values()
print("Values:", list(values))
#Control structures
if number > 5:
    print("Number is greater than 5")
else:
    print("Number is 5 or less")
for fruit in fruits:
    print("Fruit:", fruit)
count = 0
while count < 3:
    print("Count:", count)
    count += 1
#Function definition and usage
def greet(name):
    return "Hello, " + name + "!"
greeting = greet("Bob")
print(greeting)
#Class definition and usage
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof! Woof!"
myDog = Dog("Buddy", 3)
print("Dog's Name:", myDog.name)
print("Dog's Age:", myDog.age)
print(myDog.bark())
#File operations
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python file operations are easy!\n")
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
#Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")
#Importing modules
import math
sqrtValue = math.sqrt(16)
print("Square root of 16 is:", sqrtValue)
from datetime import datetime
currentTime = datetime.now()
print("Current Date and Time:", currentTime)
#List comprehensions
squaredNumbers = [x**2 for x in range(5)]
print("Squared Numbers:", squaredNumbers)
#Lambda functions
add = lambda a, b: a + b
print("Lambda Add:", add(5, 3))
#Map and filter
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled Numbers:", doubled)
evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", evenNumbers)
#Generators
def generate_numbers(n):
    for i in range(n):
        yield i
gen = generate_numbers(5)
print("Generated Numbers:", list(gen))
#List slicing
slicedFruits = fruits[1:3]
print("Sliced Fruits:", slicedFruits)   
#Tuples
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)
#Sets
uniqueFruits = set(fruits)
print("Unique Fruits Set:", uniqueFruits)
#Boolean operations
isAdult = True
isStudent = False
canAccess = isAdult and not isStudent
print("Can Access:", canAccess)
#Type casting
numStr = "100"
numInt = int(numStr)
print("Converted Integer:", numInt)
numFloat = float(numStr)
print("Converted Float:", numFloat)
strFromNum = str(numInt)
print("Converted String:", strFromNum)
#Comments
# This is a single-line comment
"""
This is a multi-line comment
spanning multiple lines.
"""
print("End of Basics")