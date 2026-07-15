#  number = input("Enter a number: ")
#  result = number + 5
#  print(result)

# Error message: TypeError: can only concatenate str (not "int") to str
# The cause: The input is read as a string, but we're trying to add an integer to it.
# Fix: I converted the input to an integer

number = int(input("Enter a number: "))
result = number + 5
print(result)