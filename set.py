# Create a set of 5 numbers and print the set.

numbers = {10, 20, 30, 40, 50}
print(numbers)


# Write a program to add "Delhi" to the set {"Mumbai", "Chennai"}.
cities = {"Mumbai", "Chennai"}
cities.add("Delhi")
print(cities)

# Create a set of subjects and remove "Science" from it.
subjects = {"Maths", "Science", "English"}
subjects.remove("Science")
print(subjects)
#
#  Write a program to check whether 50 exists in the set {10, 20, 30, 40, 50}.
numbers = {10, 20, 30, 40, 50}
print(50 in numbers)

# Create two sets {1, 2, 3} and {3, 4, 5} and print their union.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# Write a program to print the common elements from the sets {1, 2, 3} and {2, 3, 4}.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))

# Create a set of mobile brands and print the total number of items.
brands = {"Samsung", "Apple", "Vivo", "OnePlus"}
print(len(brands))

# Write a program to clear all elements from a set.
numbers = {10, 20, 30, 40}
numbers.clear()
print(numbers)
# Create a set {10, 20, 30} and add multiple values to it.
numbers = {10, 20, 30}
numbers.update([40, 50, 60])
print(numbers)

# Write a program to convert the list [1, 2, 2, 3, 3, 4] into a set.

numbers = [1, 2, 2, 3, 3, 4]
numbers = set(numbers)
print(numbers)