#Create a program that stores your name in a string and prints it in uppercase.

name = input("Enter your name: ")
print(name.upper())

#Write a program to store a sentence and print only the first character and last character.
sentence = input("Enter a sentence: ")

print("First character:", sentence[0])
print("Last character:", sentence[-1])

#Create a string "Python Programming" and print the total number of characters using a string method.

string = "Python Programming"
print(len(string))

#store "hello world" in a variable and print it with the first letter of each word capitalized.

text = "hello world"
print(text.title())

#Write a program to replace all spaces in a sentence with -.

sentence = input("Enter a sentence: ")
print(sentence.replace(" ", "-"))

#Create a string "banana" and print how many times the letter "a" appears.
text = "banana"
print(text.count("a"))

#Store your favorite movie name in a string and print it in lowercase.
movie = "Titanic"
print(movie.lower())
