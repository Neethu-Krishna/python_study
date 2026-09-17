# Create a tuple of 5 numbers and print the first number.
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
# Write a program to create a tuple of student names and print the last name.

students = ("Anu", "Rahul", "Neethu", "Arun", "Meera")
print(students[-1])

# Create a tuple (10, 20, 30, 40) and print its length.

numbers = (10, 20, 30, 40)
print(len(numbers))
# Store 5 country names in a tuple and check whether "India" exists in it.

countries = ("India", "USA", "Japan", "Canada", "Australia")
print("India" in countries)
# Create a tuple of numbers and print the maximum value.

numbers = (10, 50, 20, 80, 30)
print(max(numbers))

# Write a program to count how many times 5 appears in the tuple (1, 5, 2, 5, 3).

numbers = (1, 5, 2, 5, 3)
print(numbers.count(5))

# Create two tuples (1, 2) and (3, 4) and combine them.

tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = tuple1 + tuple2
print(tuple3)

# Store 4 animal names in a tuple and print them in sorted order.

animals = ("Dog", "Cat", "Elephant", "Bear")
animals = sorted(animals)
print(animals)
# Create a tuple ("Python", "Java", "C++") and print the index of "Java".

languages = ("Python", "Java", "C++")
print(languages.index("Java"))

# Write a program to convert the tuple (10, 20, 30) into a list.

numbers = (10, 20, 30)
numbers = list(numbers)
print(numbers)