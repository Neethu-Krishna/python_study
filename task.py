# Task 1: Student Management System
# Write a Python program to create a Student Management System using list, dictionary, tuple, functions, for loop, and while loop. Use a list to store all student records and store each student as a dictionary containing name, age, and marks. Store the marks as a tuple. Create functions to add student details, display all students, calculate average marks, and find the topper. Use a for loop to display student details and a while loop to repeatedly show the menu until the user chooses to exit. The menu should contain options such as Add Student, Display Students, Find Topper, and Exit.

# students = []


# def add_student():
#     name = input("Enter student name: ")
#     age = int(input("Enter student age: "))

#     mark1 = int(input("Enter mark 1: "))
#     mark2 = int(input("Enter mark 2: "))
#     mark3 = int(input("Enter mark 3: "))

#     marks = (mark1, mark2, mark3)

#     student = {
#         "name": name,
#         "age": age,
#         "marks": marks
#     }

#     students.append(student)

#     print("Student added successfully!")


# def display_students():
#     if len(students) == 0:
#         print("No students available.")
#     else:
#         for student in students:
#             print("Name:", student["name"])
#             print("Age:", student["age"])
#             print("Marks:", student["marks"])
#             print("----------------")


# def calculate_average(marks):
#     total = sum(marks)
#     average = total / len(marks)
#     return average


# def find_topper():
#     if len(students) == 0:
#         print("No students available.")
#     else:
#         topper = students[0]

#         for student in students:
#             if calculate_average(student["marks"]) > calculate_average(topper["marks"]):
#                 topper = student

#         print("Topper:", topper["name"])
#         print("Marks:", topper["marks"])
#         print("Average:", calculate_average(topper["marks"]))


# while True:

#     print("\n--- Student Management System ---")
#     print("1. Add Student")
#     print("2. Display Students")
#     print("3. Find Topper")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_student()

#     elif choice == "2":
#         display_students()

#     elif choice == "3":
#         find_topper()

#     elif choice == "4":
#         print("Program exited.")
#         break

#     else:
#         print("Invalid choice.")

# Task 2: ATM Machine
# Write a Python program to create a simple ATM Machine using functions, if-else, and a while loop. The program should display a menu repeatedly until the user chooses to exit. Include the following five options: Check Balance, Deposit Money, Withdraw Money, Change PIN, and Exit. Use variables to store the account balance and PIN. Create separate functions for each operation and display appropriate messages for successful and invalid transactions.

balance = 5000
pin = "1234"


def check_balance():
    print("Current balance:", balance)


def deposit_money():
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Money deposited successfully.")
        print("New balance:", balance)
    else:
        print("Invalid amount.")


def withdraw_money():
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance = balance - amount
        print("Money withdrawn successfully.")
        print("Remaining balance:", balance)


def change_pin():
    global pin

    old_pin = input("Enter old PIN: ")

    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        pin = new_pin
        print("PIN changed successfully.")
    else:
        print("Incorrect old PIN.")


while True:

    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        change_pin()

    elif choice == "5":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice.")

# Task 3: Calculator Program
# Write a Python program to create a simple Calculator using functions, if-else, and a while loop. The program should repeatedly display a menu until the user chooses to exit. Include the following five options: Addition, Subtraction, Multiplication, Division, and Exit. Create separate functions for each operation and take two numbers as input from the user. Display the result for each calculation and show an appropriate message for invalid choices or division by zero.

def addition():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 + num2

    print("Result:", result)


def subtraction():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 - num2

    print("Result:", result)


def multiplication():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 * num2

    print("Result:", result)


def division():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result:", result)


while True:

    print("\n--- CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addition()

    elif choice == "2":
        subtraction()

    elif choice == "3":
        multiplication()

    elif choice == "4":
        division()

    elif choice == "5":
        print("Calculator closed.")
        break

    else:
        print("Invalid choice.")


# Python Interview Programming Questions:


# 1. Write a Python program to check whether the string is Symmetrical or Palindrome.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


length = len(string)

if length % 2 == 0:
    middle = length // 2

    first_half = string[:middle]
    second_half = string[middle:]

    if first_half == second_half:
        print("Symmetrical")
    else:
        print("Not Symmetrical")
else:
    print("Not Symmetrical")

# 2. Write a Python program to print a given sentence in reverse order, and if it contains
# one word, reverse the characters.

sentence = input("Enter a sentence: ")

words = sentence.split()

if len(words) == 1:
    print(words[0][::-1])
else:
    print(" ".join(words[::-1]))

# 3. Check if a given string is a binary string or not (i.e., contains only 0 and 1).
string = input("Enter a string: ")

is_binary = True

for char in string:
    if char != "0" and char != "1":
        is_binary = False
        break

if is_binary:
    print("Binary string")
else:
    print("Not a binary string")

# 4. Find the maximum occurring substring in a text from a list of substrings.

text = "python is easy. python is powerful. python is popular."

substrings = ["python", "is", "easy"]

highest_count = 0
maximum_substring = ""

for word in substrings:
    count = text.count(word)

    if count > highest_count:
        highest_count = count
        maximum_substring = word

print("Maximum occurring substring:", maximum_substring)
print("Count:", highest_count)
# 5. Check if two strings are rotationally equivalent.
# 6. Remove duplicate substrings of length 3 from a string, keeping only the first
# occurrence.
# 7. Identify the character(s) which occur the second-highest number of times in a
# string.

string = input("Enter a string: ")

frequency = {}

for char in string:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

values = list(frequency.values())
values = list(set(values))
values.sort(reverse=True)

if len(values) < 2:
    print("No second-highest frequency")
else:
    second_highest = values[1]

    print("Characters with second-highest frequency:")

    for char in frequency:
        if frequency[char] == second_highest:
            print(char)
# 8. Write a function to shift characters in a string by n positions to the right.
# 9. Print numbers divisible by 3 but not divisible by 2 from a list.
numbers = [3, 4, 6, 9, 10, 12, 15, 18]

for number in numbers:

    if number % 3 == 0 and number % 2 != 0:
        print(number)

# 10. Write a recursive function to calculate the power of a number.
# 11. Write a recursive function to calculate the factorial of a number.
# 12. Compute the LCM of two numbers using a function.
# 13. Print a star triangle pattern based on the number of rows as input.
# 14. Write a program to check if a number is an Armstrong number.

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

# 15. Find all unique pairs of numbers from a list that add up to 10.

numbers = [2, 3, 4, 6, 7, 8, 5, 5]

pairs = []

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == 10:

            pair = (numbers[i], numbers[j])

            if pair not in pairs:
                pairs.append(pair)


print("Unique pairs:")

for pair in pairs:
    print(pair)

# 16. Write a function to calculate the square root of a number without using built-in
# functions.
# 17. Change a string such that the first and last characters are exchanged.

def exchange_first_last(string):

    if len(string) <= 1:
        return string

    result = string[-1] + string[1:-1] + string[0]

    return result


string = input("Enter a string: ")

print("Result:", exchange_first_last(string))
# 18. Write a function that checks if a number is a prime number.
# 19. Calculate the mean and median of a list without using in-built functions.
# 20. Create a pandas DataFrame and identify the second-lowest salary from the data.
# 21. Use a lambda function to create a new column in a DataFrame based on certain
# conditions.
# 22. Write a function to scale input data to the range 0 to 1.

# 23. Write a function to scale input data to the range -1 to 1.
# 24. Scale input data so that it has mean 0 and standard deviation 1.
# 25. From a dictionary, drop key-value pairs that are below the average value.
# 26. Remove elements from a list that occur three or more times consecutively.
# 27. Print all possible combinations from three digits.
# 28. Drop tuples from a list that contain 3 or more occurrences of the number 4.
# 29. Calculate Euclidean and Cosine distance between two 3D vectors without built-in
# functions.
# 30. Write a function to return the slope of a line given a point and y-intercept.
# 31. Print all sentences from a list that start with “i” (any case) and have at least 5 words.
# 32. Reverse all strings in a list except those of length 3.
# 33. Drop duplicate elements from a list, both with and without using set.
# 34. Check if two strings are anagrams (ignoring case).
# 35. Calculate the edit distance between two strings.
# 36. Implement string compression (e.g., "aabbbccc" → "a2b3c3").
# 37. Find the longest substring without duplicate characters.
# 38. Find the number of occurrences of a substring in a larger string.
# 39. Calculate the Jaccard similarity coefficient between two sets.
# 40. Find common elements in two sets that are greater than n.
# 41. Return a dictionary with frequency count of each element in a list.
