# Find the factorial of a number.
number = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= number:
    factorial = factorial * i
    i = i + 1

print("Factorial =", factorial)

# Generate the Fibonacci series up to N terms.
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c
    
    i = i + 1
# Check if a number is an Armstrong number.
number = int(input("Enter a number: "))

original = number
digits = len(str(number))
total = 0

while number > 0:
    digit = number % 10
    total = total + digit ** digits
    number = number // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# Check if a number is prime using a while loop.
number = int(input("Enter a number: "))

i = 1
count = 0

while i <= number:
    if number % i == 0:
        count = count + 1
    
    i = i + 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
# Print all prime numbers between 1 and N.
n = int(input("Enter N: "))

number = 2

while number <= n:
    i = 1
    count = 0

    while i <= number:
        if number % i == 0:
            count = count + 1
        
        i = i + 1

    if count == 2:
        print(number)

    number = number + 1

# Find the Greatest Common Divisor (GCD) of two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

i = 1
gcd = 1

while i <= num1 and i <= num2:
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
    
    i = i + 1

print("GCD =", gcd)
# Find the Least Common Multiple (LCM) of two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    lcm = num1
else:
    lcm = num2

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    
    lcm = lcm + 1

print("LCM =", lcm)
# Convert a decimal number to binary.
number = int(input("Enter a decimal number: "))

binary = ""

while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number = number // 2

print("Binary =", binary)

# Convert a binary number to decimal.
number = int(input("Enter a decimal number: "))

binary = ""

while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number = number // 2

print("Binary =", binary)

# Find the frequency of a digit in a number.
number = int(input("Enter a number: "))
search = int(input("Enter digit to search: "))

count = 0

while number > 0:
    digit = number % 10
    
    if digit == search:
        count = count + 1
    
    number = number // 10

print("Frequency =", count)

# Remove all zeros from a number.
number = int(input("Enter a number: "))

result = ""

while number > 0:
    digit = number % 10
    
    if digit != 0:
        result = str(digit) + result
    
    number = number // 10

print("After removing zeros =", result)

# Count even and odd digits in a number.
number = int(input("Enter a number: "))

even = 0
odd = 0

while number > 0:
    digit = number % 10
    
    if digit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    
    number = number // 10

print("Even digits =", even)
print("Odd digits =", odd)

# Find the second largest digit in a number.
number = int(input("Enter a number: "))

largest = -1
second = -1

while number > 0:
    digit = number % 10

    if digit > largest:
        second = largest
        largest = digit
    elif digit > second and digit != largest:
        second = digit

    number = number // 10

print("Largest digit =", largest)
print("Second largest digit =", second)

# Calculate the power a^b without using built-in functions.
a = int(input("Enter a: "))
b = int(input("Enter b: "))

result = 1
i = 1

while i <= b:
    result = result * a
    i = i + 1

print("Answer =", result)

# Keep asking the user for numbers until they enter 0, then print the sum.
total = 0

number = int(input("Enter a number: "))

while number != 0:
    total = total + number
    
    number = int(input("Enter a number: "))

print("Sum =", total)

# SOLVE USING WHILE LOOP

# 1. Print the following pattern using a while loop:

# *
# **
# ***
# ****
# *****

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print("*", end="")
        j += 1

    print()
    i += 1

# 2. Print the following pattern using a while loop:

# *****
# ****
# ***
# **
# *

i = 5

while i >= 1:
    j = 1

    while j <= i:
        print("*", end="")
        j += 1

    print()
    i -= 1

# 3. Print the following pattern using a while loop:

# 1
# 12
# 123
# 1234
# 12345

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(j, end="")
        j += 1

    print()
    i += 1

# 4. Print the following pattern using a while loop:

# 1
# 22
# 333
# 4444
# 55555

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(i, end="")
        j += 1

    print()
    i += 1

# 5. Print Floyd's Triangle using a while loop:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

i = 1
num = 1

while i <= 5:
    j = 1

    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1

    print()
    i += 1

# 6. Print the following pattern using a while loop:

# 12345
# 1234
# 123
# 12
# 1

12345
1234
123
12
1

# 7. Print the following pyramid using a while loop:

#     *
#    ***
#   *****
#  *******
# *********

i = 1

while i <= 5:
    
    # spaces
    space = 1
    while space <= 5 - i:
        print(" ", end="")
        space += 1

    # stars
    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    print()
    i += 1

# 8. Print the following inverted pyramid using a while loop:

# *********
#  *******
#   *****
#    ***
#     *

i = 5

while i >= 1:

    # spaces
    space = 1
    while space <= 5 - i:
        print(" ", end="")
        space += 1

    # stars
    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    print()
    i -= 1

# 9. Print the following hollow square using a while loop:

# *****
# *   *
# *   *
# *   *
# *****

i = 1

while i <= 5:
    j = 1

    while j <= 5:

        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end="")
        else:
            print(" ", end="")

        j += 1

    print()
    i += 1



# 10. Print the following square using a while loop:

# *****
# *****
# *****
# *****
# *****
i = 1

while i <= 5:
    j = 1

    while j <= 5:
        print("*", end="")
        j += 1

    print()
    i += 1


# 11. Print the following pattern using a while loop:

# A
# AB
# ABC
# ABCD
# ABCDE

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(chr(64 + j), end="")
        j += 1

    print()
    i += 1

# 12. Print the following pattern using a while loop:

# ABCDE
# ABCD
# ABC
# AB
# A
i = 5

while i >= 1:
    j = 1

    while j <= i:
        print(chr(64 + j), end="")
        j += 1

    print()
    i -= 1


# 13. Print the following pattern using a while loop:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(i, end=" ")

        j += 1

    print()
    i += 1


# 14. Print the following pattern using a while loop:

# 5
# 54
# 543
# 5432
# 54321

i = 1

while i <= 5:
    j = 5

    while j >= 6 - i:
        print(j, end="")
        j -= 1

    print()
    i += 1

# 15. Print the following pattern using a while loop:

#     1
#    121
#   12321
#  1234321
# 123454321

i = 1

while i <= 5:

    # spaces
    space = 1

    while space <= 5 - i:
        print(" ", end="")
        space += 1

    # increasing numbers
    j = 1

    while j <= i:
        print(j, end="")
        j += 1

    # decreasing numbers
    j = i - 1

    while j >= 1:
        print(j, end="")
        j -= 1

    print()
    i += 1

# 16. Print the following hollow rectangle using a while loop:

# ******
# *    *
# *    *
# ******
i = 1

while i <= 4:
    j = 1

    while j <= 6:

        if i == 1 or i == 4 or j == 1 or j == 6:
            print("*", end="")
        else:
            print(" ", end="")

        j += 1

    print()
    i += 1