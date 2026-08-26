try:
    with open('../data/missing.txt', 'r') as file: 
        pass
except FileNotFoundError:
    print ('Error: "missing.txt" was not found. Please check the file path and try again.')