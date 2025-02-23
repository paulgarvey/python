# Chapters 9 to 15, detailing - ID functions, data types and structures, Strings, String Concatenation, Numeric Types, Boolean Values, Magic Methods and Lists in python

# Python is a dynamically typed language, meaning that you do not have to declare the type of a 
# variable when you create one. Python automatically assigns the data type to the variable based 
# on the value it is assigned. 

# Immutable and Mutable objects
# Types of immutable objects are string, integer, float, boolean, nonetype and tuple.
# Types of mutable objects are list, dictionary, set, and user-defined classes.

# Built in ID() function (always returns a unique id for each object, an integer)
# The id() function returns a unique id for the specified object.
my_name = "Paul"
print(id(my_name))

my_name = your_name = "Paul"
print(id(your_name)) # same id as my_name, prints the same id

my_num = 777
print(id(my_num))

other_num = my_num
print(id(other_num)) # same id as my_num, prints the same id

print(id(my_num) == id(other_num)) # True (== is a comparison operator)


#Built in Variables
str
int
bool
list
dict

my_num = 666
print(type(my_num)) # <class 'int'>
print(type(my_num) == int) # True


print(type(int)) # <class 'type'>
print(type(str)) # <class 'type'>
print(type(bool)) # <class 'type'>
print(type(list)) # <class 'type'>
print(type(dict)) # <class 'type'>


#isinstance() function
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
print(isinstance(666, int)) # True
print(isinstance(666, str)) # false
print(isinstance(666, object)) # True
print(isinstance("Paul", object)) # True
print(isinstance("Paul", str)) # True


#Strings
