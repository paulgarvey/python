# Chapters 5 to 8, detailing - PEP8, Expressions, Statements, and Variables in python

def print_num(num):
    print(num)

print_num(5)

if 10 > 5:
    print("10 is greater than 5")
    print(True)


    # Chapter 6 - Comments
    # This is a single line comment

    # this a multi-line comment
    # this is the second line
    # this is the third line
    print("Hello, there!")
    print("Hi, there!") # this is a comment
    print("Paul")

    # Chapter 7 - Expressions 
# A statement in python is a line of code that performs an action, e.g. print("Hello, there!"), or a = 10, or import of a module
# An expression is a statement that returns a value, e.g. 10 + 20, or 10 * 20

    a = 10 / 2
    print(a) 

    res = print() # returns none

    num = int(input("Enter any n number: "))

    print(num)
    print(type(num))


import datetime

print(datetime.MAXYEAR)
  

def greet():
    return "Hello, there!"

message = greet()
print(message)



# Chapter 8 - Variables
# Variables
# A variable is a container for storing data values.
# Variables make it possible to store data values and retrieve them later in the program.

my_number = 10 # example of a variable
print(my_number)

my_boolean = True
print(my_boolean)



def print_city(city):
    print(city)  # Now it correctly prints the passed argument

favorite_city = "New York"
print_city(favorite_city)  # Prints: New York

favorite_city = "Paris"
print_city(favorite_city)  # Prints: Paris


