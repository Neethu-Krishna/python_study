# Create a dictionary with keys "name" and "age" and print the values.

student ={
    "name":"neethu",
    "age":28
}
print(student["name"])
print(student["age"])

# Write a program to create a dictionary of student details and print the student's name.

student_details ={
    "name":"neethu",
    "age":28,
    "address":"bhavanam"
}
print(student_details["name"])


# Create a dictionary of 3 subjects and marks, then print all the keys.

marks ={
    "python":78,
    "java":90,
    "cpp":98
}
print(marks.keys())

# Write a program to add a new key "city" to a dictionary.

student={
    "name":"neethu",
    "age":78
}
student["city"]="kalanjoor"
print(student)

# Create a dictionary {"a": 10, "b": 20} and change the value of "b" to 50.

number ={
    "a":10,
    "b":20
}
number["b"]=50
print(number)
# Write a program to remove the key "age" from a dictionary.

student={
    "name":"neethu",
    "age":90
}
del student["age"]
print(student)


# Create a dictionary of employee details and print all values.

employee = {
    "name": "neethu",
    "age": 30,
    "salary": 40000,
    "city": "Kochi"
}

print(employee.values())

# Write a program to check whether the key "salary" exists in a dictionary.

employee = {
    "name": "Rahul",
    "age": 30,
    "salary": 40000,
    "city": "Kochi"
}

if "salary" in employee:
    print("exists")
else:
    print("not")    

# Create two dictionaries and combine them into one dictionary.

dict1={
    "name":"neethu",
    "age":90
}
dict2={
    "course":"krishna",
    "mark":89
}
dict3=dict1|dict2
print(dict3)

# Write a program to print the total number of key-value pairs in a dictionary.
student={
    "name":"neethu",
    "age":90,
    "course":"cpp"
}
print(len(student))

# Sort the list based on the frequency of each color (highest frequency first).

colors = ["red", "blue", "red", "green", "blue", "red", "yellow"]
result = sorted(colors,key=colors.count,reverse=True)
print(result)

#Sort the list according to the number of occurrences of each element.
numbers = [5, 2, 5, 1, 2, 5, 3]
result=sorted(numbers,key=numbers.count,reverse=True)
print(result)

#Remove the leading and trailing spaces from the string and convert it to uppercase.
text = "    Python Programming    "
result = text.strip().upper()
print(result)

#Replace multiple spaces in the string with a single space.
text = "Python   Programming   Language"
result=" ".join(text.split())
print(result)

#Sort the words according to their length.
words = ["apple", "banana", "kiwi", "grapes", "orange"]
result=sorted(words,key=len)
print(result)

#Sort the names without considering uppercase and lowercase letters.
names = ["John", "alice", "David", "bob", "Emma"]
result=sorted(names,key=str.lower)
print(result)

#Sort the numbers according to their absolute values.
numbers = [-10, 5, -2, 8, -15]
result = sorted(numbers, key=abs)
print(result)

#Sort the characters of the string in alphabetical order and join them back into a string.
text = "banana"
result="".join(sorted(text))
print(result)

#Remove all spaces from the string.
text = "python programming"
result=text.replace(" ","")
print(result)

#Count the number of spaces in the string.
text = "Python Programming Language"
result=text.count(" ")
print(result)

#Convert the following comma-separated string into a list.
text = "apple,banana,orange,mango"
result=text.split(",")
print(result)

#join all the words using " | " as the separator.
words = ["Python", "Java", "C++", "JavaScript"]
result=" | ".join(words)
print(result)

#Find the most frequently occurring number using count() and sorted().
numbers = [10, 20, 20, 30, 40, 40, 40]
result=sorted(numbers,key=numbers.count,reverse=True)
print(result)

#Sort the words by their length in descending order.
words = ["cat", "apple", "dog", "elephant", "ant"]
result=sorted(words,key=len,reverse=True)
print(result)

#sort the cities according to the number of characters in each city name.
cities = ["Delhi", "Mumbai", "Pune", "Chennai", "Goa"]
result=sorted(cities,key=len)
print(result)

#Sort the numbers according to the number of digits.
numbers = [123, 45, 6789, 1, 56]






#Convert the string to lowercase and replace spaces with underscores (_).
text = "Welcome To Python"
result=text.lower().replace(" ","_")
print(result)

#Create a dictionary showing the count of each color.
colors = ["red", "blue", "red", "green", "blue", "yellow"]
result={
    "red":colors.count("red"),
    "blue":colors.count("blue"),
    "green":colors.count("green"),
    "blue":colors.count("blue"),
    "yellow":colors.count("yellow")
}
print(result)

#Sort the following list according to the last digit of each number.
numbers = [42, 35, 18, 91, 27, 63]








#Remove duplicate words from the list and sort them alphabetically.
words = ["apple", "banana", "apple", "orange", "banana", "grapes"]
result=sorted(set(words))
print(result)

#Find the word that appears the maximum number of times in the list.
words = ["red", "blue", "red", "green", "red", "blue"]
result=max(words,key=words.count)
print(result)

#Remove leading and trailing spaces, replace multiple spaces with a single space, and convert the result to title case.
text = "   Python   Programming   Language   "
result = " ".join(text.strip().split()).title()
print(result)

#Find the count of each color and store the result in a dictionary.
colors = ["yellow", "yellow", "red", "red", "red", "blue", "blue", "blue"]
result={
    "yellow":colors.count("yellow"),
    "red":colors.count("red"),
    "blue":colors.count("blue")
}
print(result)