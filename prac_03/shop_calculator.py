"""
Shop Calculator Exercise
The program output should resemble something like:
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
"""

total = 0
num_of_items = int(input("Enter the number of items: "))
while num_of_items < 0:
    print("Invalid input.")
    num_of_items = int(input("Enter the number of items: "))
for i in range(num_of_items):
    price = float(input("Enter the price of the item: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for {} items is ${:.2f}".format(num_of_items, total))
