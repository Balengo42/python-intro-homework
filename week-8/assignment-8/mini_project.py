import csv
 
FILENAME = "../data/messy_data.csv"
 
 
def load_rows(filename):
    try:
        file = open(filename, "r", newline="")
    except FileNotFoundError:
        print(f"Error: could not find '{filename}'. Please check the file path and try again.")
        return [], []
 
    clean_rows = []
    skipped = []
 
    with file:
        reader = csv.DictReader(file)
 
        for i, row in enumerate(reader, start=1):
            if None in row:
                skipped.append(f"Row {i}: extra column detected — skipped")
                continue
 
            try:
                amount = float(row["amount"])
            except ValueError:
                skipped.append(f"Row {i}: ValueError — could not convert '{row['amount']}' to float")
                continue
            except KeyError as e:
                skipped.append(f"Row {i}: KeyError — missing column {e}")
                continue
 
            try:
                name = row["name"]
                category = row["category"]
            except KeyError as e:
                skipped.append(f"Row {i}: KeyError — missing column {e}")
                continue
 
            clean_rows.append({"name": name, "category": category, "amount": amount})
 
    return clean_rows, skipped
 
 
def print_report(clean_rows, skipped):
    attempted = len(clean_rows) + len(skipped)
 
    print("=== CSV Report ===")
    print(f"Rows attempted:  {attempted}")
    print(f"Rows parsed:      {len(clean_rows)}")
    print(f"Rows skipped:     {len(skipped)}")
    print()
 
    if skipped:
        print("Skipped rows:")
        for description in skipped:
            print(f"  {description}")
        print()
 
    print("Clean data:")
    if not clean_rows:
        print("  (no valid rows)")
    else:
        for row in clean_rows:
            print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")
 
 
if __name__ == "__main__":
    clean_rows, skipped = load_rows(FILENAME)
    if clean_rows or skipped:
        print_report(clean_rows, skipped)