import csv
import os
from datetime import datetime
import argparse
 
parser = argparse.ArgumentParser(description="Generate an expense report for a given category.")
parser.add_argument("--category", default="Food", help="Expense category to report on (default: Food)")
args = parser.parse_args()
 
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
 
matches = [r for r in reader if r["category"] == args.category]
 
total = sum(r["amount"] for r in matches)
 
today = datetime.now().strftime("%B %d, %Y")
output_path = f"{args.category.lower()}_report.txt"
 
with open(output_path, "w") as file:
    file.write(f"{args.category} Expense Report — generated {today}\n")
    for r in matches:
        file.write(f"{r['date']}: ${r['amount']:.2f}\n")
    file.write(f"Total: ${total:.2f}\n")
 
print(f"Wrote {output_path} ({len(matches)} entries, total ${total:.2f})")