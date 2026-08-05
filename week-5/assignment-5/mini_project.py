numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while numbers:
    print("\nMenu:")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search")
    print("4. Sort")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        #The minimum value
        minimum = numbers[0]
        for num in numbers:
            if num < minimum:
                minimum = num
        print(f"The minimum value in the list is: {minimum}")

    elif choice == '2':
        #The maximum value
        maximum = numbers[0]
        for num in numbers:
            if num > maximum:
                maximum = num
        print(f"The maximum value in the list is: {maximum}")

    elif choice == '3':
        #Search for a number
        search_num = int(input("Enter a number to search for: "))
        result = None
        for index, num in enumerate(numbers):
            if num == search_num:
                result = index
                break

        if result is not None:
            print(f"Found {search_num} at index {result}.")
        else:
            print(f"{search_num} was not found in the list.")

    elif choice == '4':
        #Sorting the list
        n = len(numbers)
        for i in range(n-1):
            for j in range(n-1-i):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        print(f"The sorted list is: {numbers}")

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
