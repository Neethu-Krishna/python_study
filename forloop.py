# For Loop Questions

# Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

# Print all even numbers from 2 to 20.
for i in range(2, 21, 2):
    print(i)

# Print all odd numbers from 1 to 15.
for i in range(1, 16, 2):
    print(i)
# Print the multiplication table of 5.
for i in range(1, 11):
    print(5, "*", i, "=", 5 * i)

# Print each character of the string "Python" on a new line.
text = "Python"

for i in text:
    print(i)

# Find the sum of numbers from 1 to 10.
sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum =", sum)

# Print the squares of numbers from 1 to 10.
for i in range(1, 11):
    print(i, "=", i * i)
# Count how many times the letter "a" appears in "banana".
text = "banana"
count = 0

for i in text:
    if i == "a":
        count = count + 1

print("Count =", count)
# Print all items in the list ["Book", "Pen", "Pencil", "Eraser"].
items = ["Book", "Pen", "Pencil", "Eraser"]

for item in items:
    print(item)
# Print numbers from 10 to 1 in reverse order.
for i in range(10, 0, -1):
    print(i)
# For Loop Practice Questions

# Reverse the digits of a number.
number = int(input("Enter a number: "))

reverse = 0

for i in range(len(str(number))):
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse =", reverse)
# Check whether a number is an Armstrong number.
number = int(input("Enter a number: "))

original = number
digits = len(str(number))
total = 0

for i in range(digits):
    digit = number % 10
    total = total + digit ** digits
    number = number // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# Check whether a number is a palindrome.
number = int(input("Enter a number: "))

original = number
reverse = 0

for i in range(len(str(number))):
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
# Count the number of digits in a number.
number = int(input("Enter a number: "))

count = 0

for i in str(number):
    count = count + 1

print("Number of digits =", count)
# Find the sum of digits of a number.
number = int(input("Enter a number: "))

total = 0

for i in str(number):
    total = total + int(i)

print("Sum of digits =", total)
# Find the largest digit in a number.
number = input("Enter a number: ")

largest = 0

for i in number:
    if int(i) > largest:
        largest = int(i)

print("Largest digit =", largest)
# Find the sum of all even numbers in a given range.
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

total = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        total = total + i

print("Sum of even numbers =", total)
# Print all leap years between two given years.
start = int(input("Enter starting year: "))
end = int(input("Enter ending year: "))

for year in range(start, end + 1):

    if year % 400 == 0:
        print(year)

    elif year % 100 == 0:
        continue

    elif year % 4 == 0:
        print(year)
# Find the average of n numbers entered by the user.
n = int(input("How many numbers? "))

total = 0

for i in range(n):
    number = int(input("Enter number: "))
    total = total + number

average = total / n

print("Average =", average)
# Check whether a number is prime.
number = int(input("Enter a number: "))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
# Print all prime numbers between 1 and 100.
for number in range(2, 101):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1

    if count == 2:
        print(number)
# Find the GCD (HCF) of two numbers using a loop.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD =", gcd)
# Find the LCM of two numbers using a loop.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    lcm = num1
else:
    lcm = num2

for i in range(lcm, num1 * num2 + 1):

    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break

print("LCM =", lcm)


# Pattern Questions


# Print the following pattern:
# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


# Print the following pattern:
# *****
# ****
# ***
# **
# *

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# Print the following pattern:
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Print the following pattern:
# 5
# 54
# 543
# 5432
# 54321

for i in range(1, 6):
    for j in range(5, 5 - i, -1):
        print(j, end="")
    print()


# Print the following pattern:
#     *
#    ***
#   *****
#  *******
# *********


for i in range(1, 6):
    
    for j in range(5 - i):
        print(" ", end="")
    
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()

# Print the following pattern:
# 1
# 22
# 333
# 4444
# 55555

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()