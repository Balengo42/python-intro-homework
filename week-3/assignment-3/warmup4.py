number= int(input("Enter a number: "))
if number == 0:
    parity="even"
    sign="zero"

elif number % 2 == 0:
    parity="even"
    if number < 0:
        sign="negative"
    else:
        sign="positive"

elif number % 2 != 0:
    parity="odd"
    if number < 0:
        sign="negative"
    else:
        sign="positive"
    
print("Enter a number: ", number)
print(f"{number} is {sign}.")
print(f"{number} is {parity}.")

