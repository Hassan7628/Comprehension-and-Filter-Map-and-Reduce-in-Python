print("\n\n")

# Number1:
values = []
for x in range(1, 10):
    values.append(x)

print(values, "\n")

# Comprehension:
values2 = [x + 1 for x in range(9)]
print(values2, "\n")


# Number2:
# get all even number:
even_num = []
for num in range(50):
    is_even = num % 2 == 0

    if is_even:
        even_num.append(num)

print(even_num, "\n")

# Comprehension:
even_num2 = [num for num in range(50) if num % 2 == 0]
print(even_num2, "\n")


# Number3:
# strings that start with letter 'a' and end with letter 'y':
options = ["apple", "any", "not", "banana", "nany", "albany"]

filter_list = []
for string in options:
    if len(string) <= 2:
        continue

    if string[0].lower() != "a":
        continue

    if string[-1].lower() != "y":
        continue

    filter_list.append(string)

print(filter_list, "\n")

# Comprehension:
filter_list2 = [
    string
    for string in options
    if len(string) >= 2 and string[0] == "a" and string[-1] == "y"
]
print(filter_list2, "\n")


# Number4:
# Flattening a matrix (list of lists):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = []
for row in matrix:
    for num in row:

        flattened_list.append(num)

print(flattened_list, "\n")

# Comprehension:
flattened_list2 = [num for row in matrix for num in row]
print(flattened_list2, "\n")


# Number5:
# Categorize numbers as even and odd:
categories = []
for num in range(10):
    if num % 2 == 0:
        categories.append("Even")

    else:
        categories.append("Odd")

print(categories, "\n")

# Comprehension:
categories2 = ["Even" if num % 2 == 0 else "Odd" for num in range(10)]
print(categories2, "\n")


# Number6:
# Making a 3D list:
lst = []
for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)

        l1.append(l2)

    lst.append(l1)

print(lst, "\n")

# Comprehension:
lst2 = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
print(lst2, "\n")


# Number7:
# List comprehension with function:
def square(x):
    return x**2


sqr = [square(num) for num in range(5)]
print(sqr, "\n")


# Number8:
# Dictionary comprehension:
pairs = [("a", 1), ("b", 2), ("c", 3)]

my_dict = {k: v for k, v in pairs}
print(my_dict, "\n")

# Number9:
# Set Comprehension:
num_list = [2, 2, 3, 4, 2, 1, 3, 4, 5, 2, 4, 5]

unique_square = {x**2 for x in num_list}
print(unique_square, "\n")

# Number10:
# Genereator Comprehension:
sum_of_squares = sum(num**2 for num in range(1000000))
print(sum_of_squares)

print("\n\n")