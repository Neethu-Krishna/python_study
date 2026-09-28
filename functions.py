# Write a function to count the number of vowels and consonants in a given string. Ignore case and spaces.

def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text.lower():
        if ch in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1

    return vowels, consonants


text = "I Love Python"

v, c = count_vowels_consonants(text)

print("Vowels:", v)
print("Consonants:", c)
# Write a function is_isogram(text) that checks whether a string is an isogram (a word with no repeating letters, consecutive or non-consecutive).


# Write a function that takes a sentence and returns the longest word. If there are multiple words of the same maximum length, return the first one.

def longest_word(sentence):
    words = sentence.split()

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(longest_word("I love learning Python"))
# Write a function to remove all punctuation characters from a string without using the built-in string.punctuation.

# Write a function that accepts a string and returns a new string where every character is repeated twice (e.g., "cat" becomes "ccaatt").

def repeat_characters(text):
    result = ""

    for ch in text:
        result += ch * 2

    return result


print(repeat_characters("cat"))
# Write a function find_missing_number(arr, n) that takes a list of distinct integers from 1 to n (with one number missing) and returns the missing element. Do not use built-in search functions.
# Write a function that returns the second largest number in a list of integers without sorting the list or using max().

def second_largest(numbers):
    largest = float("-inf")
    second = float("-inf")

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second


numbers = [10, 5, 20, 8, 15]

print(second_largest(numbers))
# Write a function rotate_list(arr, k) that rotates a list to the left by k positions.
# Write a function that takes a list of integers and moves all zeros to the end of the list while maintaining the relative order of the non-zero elements.
# Write a function that takes two lists and returns a list of elements that are common to both, preserving the order of appearance from the first list. Do not use sets.
# Write a recursive function to compute the n-th Fibonacci number.
# Write a recursive function to find the sum of all digits of a positive integer.
# Write a function that takes an integer n and returns a list of its prime factors.
# Write a function that merges two dictionaries. If a key exists in both dictionaries, the value in the resulting dictionary should be the sum of both values.
# Write a function that takes a string and returns the first non-repeating character. If all characters repeat, return None.
# Write a function to invert a dictionary (swap keys and values). If multiple keys have the same value, group the keys into a list for that value.
# Given a dictionary of student names and their scores, write a function to return a list of students who scored above the average score.

def above_average(students):
    total = 0

    for score in students.values():
        total += score

    average = total / len(students)

    result = []

    for name, score in students.items():
        if score > average:
            result.append(name)

    return result


students = {
    "Anu": 70,
    "Binu": 80,
    "Cathy": 90,
    "David": 60
}

print(above_average(students))
# Write a function to group a list of words by their starting character, returning a dictionary where the keys are characters and the values are lists of words.