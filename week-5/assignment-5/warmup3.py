names_1 = ["Alice", "Bob", "Charlie", "David", "Eve"]
search_name = input("Enter a name to search for: ")

found = None
index = 0 
for name in names_1:
    if name == search_name:
        found = index
        break
    index += 1

if found is not None:
    print(f"Found {search_name} at index {found}.")
else:
    print(f"{search_name} was not found in the list.")