try:
    with open('../data/missing.txt', 'r') as file:
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print ("Error: 'missing.txt' was not found. Please check the file path and try again.")