age= int(input("Enter your age:"))
if age >= 65:
    group = "Senior"
elif age >= 18:
    group = "Adult"
elif age >= 13:
    group = "Teen"
else:
    group = "Child"

print("You are a", group)