"""
CP1404 - Practical 2
Test for integer input
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an integer: "))
        finished = True
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
