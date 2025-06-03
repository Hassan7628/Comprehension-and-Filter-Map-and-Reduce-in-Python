# Student Grade System:
Std = [
    {"name": "Ali", "marks": 45},
    {"name": "Ahmed", "marks": 78},
    {"name": "Shunan", "marks": 33},
    {"name": "Hassan", "marks": 88},
]


passed = list(filter(lambda x: x["marks"] >= 40, Std))

print("\nPassed Student(s):\n")
for s in passed:
    print(f"{s["name"]} : {s["marks"]}")

# Email Validator:
emails = [
    "hassan2323@gmail.com",
    "ali7364gmail.com",
    "addon@proton.me",
    "ahmed@gmailcom",
]

valid_email = list(filter(lambda x: "@" in x and "." in x.split("@")[-1], emails))
print(f"\n{valid_email}\n")

# Filter by Price and Stock:
products = [
    {"name": "Pen", "price": 10, "stock": 50},
    {"name": "Notebook", "price": 120, "stock": 0},
    {"name": "Pencil", "price": 5, "stock": 100},
    {"name": "Eraser", "price": 8, "stock": 0},
]

filtered = list(filter(lambda x: x["price"] < 100 and x["stock"] >= 1, products))

print("\nSale Items:\n")
for i in filtered:
    print(f"Name: {i['name']:>7}, Price: {i['price']:>5}, Stock: {i['stock']:>5}")

print()