# function scope
# namespace = local variables + parameters 

numbers = []
for i in range(5):
    j = int(input("Enter a number: "))
    numbers.append(j)
    i += 1

def find_max(numbers):
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


def find_min(numbers):
    assert len(numbers) > 0
    min_number = numbers[0]
    remaining = numbers[1:]
    for number in remaining:
        if number < min_number:
            min_number = number
    return min_number

print(find_max(numbers))
print(find_min(numbers))

















# A function parameter refers to the same object
# as its corresponding argument

def clear_list(data):
    print("local parameter id: ", id(data))
    data.clear()

data = [1,2,3]
print("before clear_list, data: ", data)
print("global data id: ", id(data))
clear_list(data)
print("after clear_list, data: ", data)
print()





















# Assignment breaks the relationship between the
# parameter and the corresponding argument

def clear_number(number):
    print("local number id: ", id(number))
    number = 0

number = 42
print("before clear_number, number: ", number)
print("global number id: ", id(number))
clear_number(number)
print("after clear_number: ", number)
print()






















# Functions in Python support named parameters

def make_size(width=640, height=480):
    return width, height

print(make_size(width=320, height=320))
print(make_size(height=320, width=320))

# Functions in python support default parameter values

print(make_size())
print(make_size(height=640))
print()























# Beware: mutable default parameters have side-effects

def make_list(data=[], extra_value=1):
    print("local data: ", data)
    data.append(extra_value)
    return data

data = []
print("result: ", make_list())
print("result: ", make_list())
print("result: ", make_list())
print("result: ", make_list())






















# a variable number of parameters is also possible

def print_all(value, *items):
    print(type(items))
    for item in items:
        print(item)

print_all(1,2,3,4,5)
print()















# python supports type annotations

def compute_average(items: list) -> float:
    total = 0
    for item in items:
        total += item
    return total / len(items)

print(compute_average([1,2,3,4,5]))










