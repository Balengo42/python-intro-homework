Ask= input("Enter a positive integer: ")
while not (Ask.isdigit() and int(Ask) > 0):
    print("That's not a positive integer. Try again.")
    Ask = input("Enter a positive integer: ")
print(f"Got it: {Ask}")