# Write a program to check whether a number is positive or negative.
number = int(input("enter number : "))
if number >=0:
    print("positive")
else:
    print("negative")    

# Write a program to check whether a person is eligible to vote (age 18 or above).
age = int(input("enter age :"))
if age >= 18 :
    print("eligible")
else:
    print("not eligible")

# Enter two numbers and print the greater number.
a = int(input("enter first number: "))
b = int(input("enter second number"))
if a >= b:
    print(a ,"is greatest")
else:
    print(b ,"is greatest")   

# Write a program to check whether a number is even or odd.
a = int(input("enter number: "))
if a % 2 == 0:
    print("even")
else:
    print("odd")  

# Enter a mark and display:
#              A grade for 90 and above
#              B grade for 75–89
#              C grade for 50–74
#             Fail for below 50
mark=int(input("enter mark :"))
if mark >= 90:
    print("A grade")
elif mark >= 75:
    print("b")    
elif mark >= 74:
    print("C grade")
else:
    print("fail")        

# Write a program to check whether a character is a vowel or consonant.
char = input("enter character")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("vowel")
else:
    print("consonant")    

# Enter three numbers and print the largest number.
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third  number"))
if num1 >= num2 and num1 >= num3:
    print(num1, "is largest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is largest")
else:
    print(num3, "is largest")
# Write a program to check whether a year is a leap year or not.
# Enter the temperature and display:
#              Extreme temp (above 35)
#              Warm (20–35)
#              Cold (below 20)
# Write a program to check whether a number is divisible by 5, 3, both, or neither.

# 1. Write a program to check whether a character is:
#     - Uppercase letter
#     - Lowercase letter
#     - Digit
#     - Special character

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase letter")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase letter")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special character")


# 2. Write a program to calculate income tax based on the following conditions:
#     - Income ≤ ₹2,50,000 → No tax
#     - ₹2,50,001–₹5,00,000 → 5% tax
#     - ₹5,00,001–₹10,00,000 → 20% tax
#     - Above ₹10,00,000 → 30% tax

income = int(input("Enter your income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 5 / 100
elif income <= 1000000:
    tax = income * 20 / 100
else:
    tax = income * 30 / 100

print("Tax =", tax)

# 3. Write a program to check whether three given sides can form a triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Can form a triangle")
else:
    print("Cannot form a triangle")

# 4. Write a program to identify the type of triangle based on its sides:
#     - Equilateral
#     - Isosceles
#     - Scalene

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# 5. Write a program that asks the user to enter a username and password:
#     - If both are correct, display "Login Successful".
#     - If the username is correct but the password is incorrect, display "Incorrect Password".
#     - If the username is incorrect, display "User Not Found".

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
elif username == "admin":
    print("Incorrect Password")
else:
    print("User Not Found")

# 6. Build a simple calculator using if-elif-else that performs:
#     - Addition (+)
#     - Subtraction (-)
#     - Multiplication (*)
#     - Division (/)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# 7. Write a menu-driven program with the following options:
#     1. Check Even/Odd
#     2. Find the Largest of Two Numbers
#     3. Check Leap Year
#     4. Exit

print("1. Check Even/Odd")
print("2. Find Largest of Two Numbers")
print("3. Check Leap Year")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 > num2:
        print("Largest =", num1)
    elif num2 > num1:
        print("Largest =", num2)
    else:
        print("Both are equal")

elif choice == 3:
    year = int(input("Enter year: "))

    if year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0:
        print("Not a Leap Year")
    elif year % 4 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")

elif choice == 4:
    print("Exit")

else:
    print("Invalid choice")

# 8. Write a program to calculate the Body Mass Index (BMI) of a person and display the category:
#     - Underweight
#     - Normal
#     - Overweight
#     - Obese

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 9. Write a program to calculate the discount on a purchase based on the following conditions:
#     - Purchase amount ≥ ₹5000 → 20% discount
#     - Purchase amount between ₹2000 and ₹4999 → 10% discount
#     - Purchase amount below ₹2000 → No discount

amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 2000:
    discount = amount * 10 / 100
else:
    discount = 0

print("Discount =", discount)

final_amount = amount - discount

print("Final amount =", final_amount)

# 10. Write a program to determine the result of a student based on marks in three subjects:
#     - If the student scores at least 35 marks in all subjects, display "Pass".
#     - Otherwise, display "Fail".
#     - If the student passes, classify the result based on the average marks:
#         - Average ≥ 75 → Distinction
#         - Average 60–74 → First Class
#         - Average 50–59 → Second Class
#         - Average below 50 → Pass Class
mark1 = int(input("Enter mark for subject 1: "))
mark2 = int(input("Enter mark for subject 2: "))
mark3 = int(input("Enter mark for subject 3: "))

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:

    print("Pass")

    average = (mark1 + mark2 + mark3) / 3

    print("Average =", average)

    if average >= 75:
        print("Distinction")
    elif average >= 60:
        print("First Class")
    elif average >= 50:
        print("Second Class")
    else:
        print("Pass Class")

else:
    print("Fail")
