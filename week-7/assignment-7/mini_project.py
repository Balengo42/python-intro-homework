import csv
import os
from datetime import datetime
 
path = os.path.join("..", "data", "expenses.csv")
 
if not os.path.exists(path):
    print(f"{path} not found.")
    exit()
 
try:
    with open(path, "r") as file:
        reader = list(csv.DictReader(file))
        for row in reader:
            row["amount"] = float(row["amount"])
except Exception as e:
    print(f"An error occurred while reading {path}: {e}")
    exit()
 
matches = [r for r in reader if r["category"] == "Food"]
 
total = sum(r["amount"] for r in matches)
 
today = datetime.now().strftime("%B %d, %Y")
 
with open("food_report.txt", "w") as file:
    file.write(f"Food Expense Report — generated {today}\n")
    for r in matches:
        file.write(f"{r['date']}: ${r['amount']:.2f}\n")
    file.write(f"Total: ${total:.2f}\n")
 
print(f"Wrote food_report.txt ({len(matches)} entries, total ${total:.2f})")
 