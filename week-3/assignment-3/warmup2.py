age= int(input("What is your age?"))
if age >= 65:
    group = "Senior"
elif age >= 18:
    group = "Adult"
elif age >= 13:
    group = "Teen"
else:
    group = "Child"

print("Enter your age:", age)
print("You are a", group)