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