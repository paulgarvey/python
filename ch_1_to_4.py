print("Hello Python")

print(100)
print(-20)

print(True)
print(False)

print([])
print([1, 2, 3])

print({})
print({'name': 'Paul', 'size': 'Jogn'})
print({
    'name': 'Paul',
     'size': 'John'
     })

# Functions
# A function is a block of code that only runs when it is called
# You can pass data, known as parameters, into a function`
# A function can return data as a result
 

def hello(name):
    print(name)
    print("Hello, there!")
    print("Hi, there!")

hello("Bogdan")
hello("Alice")


def add_number(a, b):
    print(a + b)

add_number(10, 20)


def add_number(a, b):
    sum = a + b
    print(sum)

add_number(12, 20)

def multiply_numbers(a, b):
    sum = a * b
    print(sum)

multiply_numbers(12, 20)


def multiply_numbers(a, b):
    result = a * b
    return result

result_of_multplication = multiply_numbers(12, 20) 
print(result_of_multplication)

print(multiply_numbers(15, 20))

# print(dir())
print(__builtins__)

print(dir(__builtins__))


print(DeprecationWarning)


#Input Function

my_name = input("Please enter your name: ")
print(my_name)


mu_number = input("Please enter a number: ")
print(mu_number)
print(type(mu_number))

print(my_name.upper())