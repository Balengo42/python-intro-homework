try:
    with open('../data/missing.txt', 'r') as file:
        print('missing.txt')
except FileNotFoundError:
    print ('Error: "missing.txt" was not found. Please check the file path and try again.")