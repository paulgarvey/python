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
# strings are an instance of the str class, e.g. "Paul"
long_str = "This it's is a very long string that \nspans multiple lines and is enclosed in double quotes"
print(long_str)
print(type(long_str)) # <class 'str'>
print(type(long_str) == str) # <class 'str'>
print(isinstance(long_str, str)) # True


my_comment = "This is my short commnet"
print(my_comment)
print(len(my_comment)) # 26print(my_comment[0]) # Zero is the first index
print(my_comment[3]) # 
print(my_comment[4]) #

my_long_comment = my_comment.replace("short", "long") # Have to create a new variable to store the new string
print(my_long_comment) # This is my short comment
print(len(my_long_comment)) # 26


my_best_comment = "This is my best comment"
print(my_best_comment.count(" ")) # there are 4 spaces in the string
print(my_best_comment.count("is")) # there are 2 "is" in the string
print(my_best_comment[4]) # i
print(my_best_comment[5]) # s
print(my_best_comment[6]) # space
print(my_best_comment[2:7]) # m
print(my_best_comment[ :10])
print(my_best_comment[:-1])
print(my_best_comment[:-10])
print(my_best_comment[4:-10])
print(my_best_comment.find("best")) # 11
print(my_best_comment.find("long")) # find method, if -1 is returned, the string is not found
print(my_best_comment.split(" ")) # this creates a list of words in the string
print(my_best_comment.upper()) # THIS IS MY BEST COMMENT
print(my_best_comment.lower()) # this is my best comment
# print(dir(my_best_comment)) # returns all the methods that can be used on the stringclear


#String Concatenation
