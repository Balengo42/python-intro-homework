Ask= input("Please enter a positive integer: ")
while not (Ask.isdigit() and int(Ask) > 0):
    Ask = input("That's not a positive integer. Try again.")
print(f"Got it: {Ask}")