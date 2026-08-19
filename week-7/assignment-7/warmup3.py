import os
print (os.getcwd())

if os.path.exists('../data/expenses.csv'):
    print("expenses.csv found")
else:
    print ("expenses.csv not found")

path = os.path.join ("..", "data", "expenses.csv")
print(path)