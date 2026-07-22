number = int(input("Enter a number: "))

# Sign block
if number == 0:
    sign = "zero"
elif number < 0:
    sign = "negative"
else:
    sign = "positive"

# Parity block
if number % 2 == 0:
    parity = "even"
else:
    parity = "odd"

print(f"{number} is {sign}.")
print(f"{number} is {parity}.")