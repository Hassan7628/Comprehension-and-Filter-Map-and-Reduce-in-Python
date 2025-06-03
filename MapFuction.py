# Currency Convertor:
usd = [22, 33, 4, 55, 32, 101]

convert = list(map(lambda x: x * 280, usd))

print("\nUSD to PKR:\n")
for pkr in convert:
    print(f"${pkr/280} : Rs{pkr}")

# Name Formatter:
names = ["HAssan", "AlI", "aHMEd", "sHUNan", "KiNzA"]

organized_name = list(map(lambda x: x.title(), names))
print(f"\nOrganized names: {organized_name}\n")

# Square Root Calculator:
numbers = [11, 22, 4, 5, 22, 101, 33, 2]

sqrt = list(map(lambda x: x**0.5, numbers))

print("\nSquare Root:\n")
for sq in sqrt:
    print(f"{sq:.2f}")

print()