# PART 1: BASIC LIST COMPREHENSIONS
# ------------------------------------------------------------------------

# 1. Given a list numbers = [1, 2, 3, 4, 5], write a list comprehension to create a new list containing the cube of each number.

numbers = [1, 2, 3, 4, 5]

result = [number ** 3 for number in numbers]

print(result)

# 2. Convert the following for loop into a single-line list comprehension:
#    degrees_celsius = [0, 10, 20, 30, 40]
#    degrees_fahrenheit = []
#    for c in degrees_celsius:
#        degrees_fahrenheit.append((c * 9/5) + 32)

numbers = [1, 2, 3, 4, 5]

result = [number ** 3 for number in numbers]

print(result)

# 3. Given a string word = "Python", create a list of its individual characters using list comprehension.

word = "Python"
result = [char for char in word]
print(result)


# 4. Write a list comprehension that generates a list of numbers from 1 to 15 that are multiplied by 10 (e.g., [10, 20, 30, ...]).

result = [number * 10 for number in range(1, 16)]
print(result)

# 5. Given a list of strings names = ['alice', 'bob', 'charlie'], use a list comprehension to capitalize the first letter of each name.

names = ['alice', 'bob', 'charlie']
result = [name.capitalize() for name in names]
print(result)


# ------------------------------------------------------------------------
# PART 2: LIST COMPREHENSIONS WITH CONDITIONALS (if)
# ------------------------------------------------------------------------

# 6. Given numbers = [12, 34, 57, 45, 66, 72, 89], write a list comprehension to extract only the numbers that are divisible by 3.

numbers = [12, 34, 57, 45, 66, 72, 89]
result = [number for number in numbers if number % 3 == 0]
print(result)

# 7. Given a list of words words = ['apple', 'pear', 'banana', 'kiwi', 'plum'], write a list comprehension to filter out words that have fewer than 5 characters.

words = ['apple', 'pear', 'banana', 'kiwi', 'plum']
result = [word for word in words if len(word) >= 5]
print(result)


# 8. Using range(1, 30), create a list of all numbers that are multiples of both 2 and 3.

result = [number for number in range(1, 30)
          if number % 2 == 0 and number % 3 == 0]

print(result)

# 9. Given a string sentence = "Learning Python is fun and rewarding", write a list comprehension to extract all the vowels (a, e, i, o, u) present in the sentence (ignoring spaces).

sentence = "Learning Python is fun and rewarding"
result = [char for char in sentence if char.lower() in "aeiou"]
print(result)

# 10. Given a list mixed_data = [1, 'hello', 2, 'world', 3.14, True], write a list comprehension to keep only the integer values.

mixed_data = [1, 'hello', 2, 'world', 3.14, True]

result = [item for item in mixed_data if type(item) == int]

print(result)


# ------------------------------------------------------------------------
# PART 3: LIST COMPREHENSIONS WITH IF-ELSE
# ------------------------------------------------------------------------

# 11. Given numbers = [1, 5, 10, 15, 20], write a list comprehension that replaces numbers greater than or equal to 10 with the string 'High', and numbers less than 10 with 'Low'.

numbers = [1, 5, 10, 15, 20]
result = ['High' if number >= 10 else 'Low' for number in numbers]
print(result)

# 12. Given a list of integers scores = [45, 82, 50, 91, 68], use an if-else list comprehension to return 'Pass' if the score is 60 or above, and 'Fail' otherwise.

scores = [45, 82, 50, 91, 68]
result = ['Pass' if score >= 60 else 'Fail' for score in scores]
print(result)

# 13. Given values = [10, -5, 3, -1, 0, -8], write a list comprehension that squares the positive numbers and leaves negative numbers (and zero) as they are.

values = [10, -5, 3, -1, 0, -8]
result = [value ** 2 if value > 0 else value for value in values]
print(result)

# 14. Given a list of names guests = ['Alex', 'bob', 'Charlie', 'david'], create a list where the names are converted to uppercase if they start with a capital letter, and lowercase if they don't.

guests = ['Alex', 'bob', 'Charlie', 'david']

result = [name.upper() if name[0].isupper() else name.lower()
          for name in guests]

print(result)

# ------------------------------------------------------------------------
# PART 4: SET AND DICTIONARY COMPREHENSIONS (BASIC)
# ------------------------------------------------------------------------

# 15. Given a sentence string text = "apple banana apple cherry banana", write a set comprehension to get a unique set of the lengths of each word.
text = "apple banana apple cherry banana"

result = {len(word) for word in text.split()}

print(result)


# 16. Convert the list colors = ['red', 'blue', 'green'] into a dictionary comprehension where the key is the color string and the value is the length of that string.

colors = ['red', 'blue', 'green']

result = {color: len(color) for color in colors}

print(result)


# 17. Given a dictionary item_prices = {'apple': 1.00, 'banana': 0.50, 'kiwi': 1.25}, write a dictionary comprehension to increase all the prices by 10%.

item_prices = {
    'apple': 1.00,
    'banana': 0.50,
    'kiwi': 1.25
}

result = {item: price * 1.10 for item, price in item_prices.items()}

print(result)

# 18. Given a list of tuples student_scores = [('Alice', 85), ('Bob', 55), ('Charlie', 92)], write a dictionary comprehension to map the student's name to their score, but only if their score is above 60.

student_scores = [
    ('Alice', 85),
    ('Bob', 55),
    ('Charlie', 92)
]

result = {
    name: score
    for name, score in student_scores
    if score > 60
}

print(result)

# 19. Write a dictionary comprehension that maps numbers from 1 to 5 to their respective squares (e.g., {1: 1, 2: 4, 3: 9, ...}).

result = {number: number ** 2 for number in range(1, 6)}

print(result)

# 20. Given a dictionary stock = {'Apples': 50, 'Oranges': 0, 'Pears': 12, 'Grapes': 0}, write a dictionary comprehension to filter out items that are out of stock (value is 0).
stock = {
    'Apples': 50,
    'Oranges': 0,
    'Pears': 12,
    'Grapes': 0
}

result = {
    item: quantity
    for item, quantity in stock.items()
    if quantity != 0
}

print(result)



# ------------------------------------------------------------------------
# PART 5: NESTED LIST COMPREHENSIONS (FLATTENING & MATRICES)
# ------------------------------------------------------------------------

# 21. Given a matrix (a list of lists) matrix = [[1, 2], [3, 4], [5, 6]], write a list comprehension to flatten it into a single list: [1, 2, 3, 4, 5, 6].

matrix = [[1, 2], [3, 4], [5, 6]]

result = [number for row in matrix for number in row]

print(result)

# 22. Write a list comprehension to create a 3x3 identity matrix (a grid where diagonal elements are 1 and all others are 0).
result = [[1 if row == column else 0 for column in range(3)]
          for row in range(3)]

print(result)

# 23. Given a list of lists containing strings groups = [['apple', 'pear'], ['banana', 'kiwi', 'plum'], ['grape']], write a nested list comprehension to filter and keep only the strings that have 5 or more characters, keeping the nested list structure intact.
groups = [
    ['apple', 'pear'],
    ['banana', 'kiwi', 'plum'],
    ['grape']
]

result = [
    [word for word in group if len(word) >= 5]
    for group in groups
]

print(result)


# 24. Given matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], write a list comprehension to transpose the matrix (swap its rows and columns), turning it into [[1, 4, 7], [2, 5, 8], [3, 6, 9]].

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [
    [matrix[row][column] for row in range(3)]
    for column in range(3)
]

print(result)


# ------------------------------------------------------------------------
# PART 6: ADVANCED CONDITIONAL LOGIC (IF-ELIF-ELSE EMULATION)
# ------------------------------------------------------------------------

# 25. Given a list of test percentages percentages = [85, 42, 73, 91, 60], use a single-line list comprehension to convert them to letter grades based on these rules:
#     - >= 90 -> 'A'
#     - >= 70 -> 'B'
#     - Otherwise -> 'C'

percentages = [85, 42, 73, 91, 60]

result = [
    'A' if percentage >= 90
    else 'B' if percentage >= 70
    else 'C'
    for percentage in percentages
]

print(result)

# 26. Given a list of mixed numbers data = [10, -3, 0, 5, -1, 0, 14], write a list comprehension that replaces positive numbers with 1, negative numbers with -1, and leaves zeros as 0.

data = [10, -3, 0, 5, -1, 0, 14]

result = [
    1 if number > 0
    else -1 if number < 0
    else 0
    for number in data
]

print(result)

# 27. Given a list of strings representing numbers and text mixed = ['10', 'apple', '20', '3.14', 'orange'], write a list comprehension that multiplies the item by 2 if it consists purely of digits (use .isdigit()), and converts it to uppercase if it is alphabetical. Drop any other types of strings.

mixed = ['10', 'apple', '20', '3.14', 'orange']

result = [
    str(int(item) * 2) if item.isdigit()
    else item.upper() if item.isalpha()
    else None
    for item in mixed
]

result = [item for item in result if item is not None]

print(result)


# ------------------------------------------------------------------------
# PART 7: ADVANCED STRING & DATA WRANGLING
# ------------------------------------------------------------------------

# 28. Given a string sentence = "The quick brown fox jumps over the lazy dog", write a list comprehension to generate a list of tuples containing each word and its length, but exclude words that are shorter than 4 characters.

sentence = "The quick brown fox jumps over the lazy dog"

result = [
    (word, len(word))
    for word in sentence.split()
    if len(word) >= 4
]

print(result)
# 29. Given a string with messy whitespace log = "  error: timeout   info: success    debug: pending ", write a list comprehension to extract a clean list of individual tokens, removing all extra trailing/leading whitespaces and empty elements.
log = "  error: timeout   info: success    debug: pending "

result = [word.strip() for word in log.split() if word.strip()]

print(result)

# 30. Given a list of email addresses emails = ['user1@gmail.com', 'admin@yahoo.com', 'user2@gmail.com', 'tech@outlook.com'], write a set comprehension to extract a unique set of just the domain names (e.g., {'gmail.com', 'yahoo.com', ...}).
emails = [
    'user1@gmail.com',
    'admin@yahoo.com',
    'user2@gmail.com',
    'tech@outlook.com'
]

result = {email.split('@')[1] for email in emails}

print(result)

# 31. Given a list of filenames files = ['index.html', 'style.css', 'script.js', 'image.png', 'main.py'], write a list comprehension to extract only the extensions (e.g., ['html', 'css', ...]) for files that end in .html or .js.

files = [
    'index.html',
    'style.css',
    'script.js',
    'image.png',
    'main.py'
]

result = [
    file.split('.')[1]
    for file in files
    if file.endswith('.html') or file.endswith('.js')
]

print(result)

# ------------------------------------------------------------------------
# PART 8: COMPLEX DICTIONARY & SET COMPREHENSIONS
# ------------------------------------------------------------------------

# 32. Given two lists of equal length keys = ['name', 'age', 'role'] and values = ['Alice', 30, 'Engineer'], combine them into a single dictionary using a dictionary comprehension without using the zip() function.


keys = ['name', 'age', 'role']
values = ['Alice', 30, 'Engineer']

result = {
    keys[i]: values[i]
    for i in range(len(keys))
}

print(result)
# 33. Given a dictionary of student grades report_card = {'Math': 90, 'Science': 55, 'History': 78, 'English': 42}, write a dictionary comprehension to invert the dictionary (swap keys and values), but only for subjects where the student passed (score >= 60).

report_card = {
    'Math': 90,
    'Science': 55,
    'History': 78,
    'English': 42
}

result = {
    score: subject
    for subject, score in report_card.items()
    if score >= 60
}

print(result)
# 34. Given a nested dictionary representing store inventory:
#     inventory = {
#         'store_A': {'apples': 10, 'bananas': 0},
#         'store_B': {'apples': 5, 'bananas': 12}
#     }
#     Write a dictionary comprehension to create a flat dictionary containing only the items that have a quantity greater than 0, formatted as {(store, item): quantity}.

inventory = {
    'store_A': {'apples': 10, 'bananas': 0},
    'store_B': {'apples': 5, 'bananas': 12}
}

result = {
    (store, item): quantity
    for store, items in inventory.items()
    for item, quantity in items.items()
    if quantity > 0
}

print(result)

# 35. Write a dictionary comprehension that takes a string word = "abracadabra" and maps each unique character to the count of its occurrences in the string.

word = "abracadabra"

result = {
    char: word.count(char)
    for char in set(word)
}

print(result)

# 36. Given a list of tuples representing products and their prices products = [('laptop', 1200), ('mouse', 25), ('keyboard', 75), ('monitor', 300)], write a dictionary comprehension to apply a 10% tax to products that cost more than 100, while keeping the original price for everything else.
products = [
    ('laptop', 1200),
    ('mouse', 25),
    ('keyboard', 75),
    ('monitor', 300)
]

result = {
    product: price * 1.10 if price > 100 else price
    for product, price in products
}

print(result)

# 37. Using a set comprehension, find all numbers between 1 and 50 that are perfect squares (e.g., 1, 4, 9...).

result = {
    number ** 2
    for number in range(1, 8)
    if number ** 2 <= 50
}

print(result)

# ------------------------------------------------------------------------
# PART 9: ENUMERATION AND COORDINATE GRIDS
# ------------------------------------------------------------------------

# 38. Given a list items = ['a', 'b', 'c', 'd'], use a dictionary comprehension alongside enumerate() to map each item to its index, but only for items at odd index positions.

items = ['a', 'b', 'c', 'd']

result = {
    item: index
    for index, item in enumerate(items)
    if index % 2 != 0
}

print(result)
# 39. Write a list comprehension to generate all possible (x, y) coordinate pairs for a grid where x goes from 0 to 3 and y goes from 0 to 3, but filter out pairs where x == y.
result = [
    (x, y)
    for x in range(4)
    for y in range(4)
    if x != y
]

print(result)

# 40. Given a text string phrase = "Python Comprehensions Are Powerful", write a list comprehension to extract the index positions of all the uppercase letters in the string.
phrase = "Python Comprehensions Are Powerful"

result = [
    index
    for index, char in enumerate(phrase)
    if char.isupper()
]

print(result)
